<script>
    import { push } from 'svelte-spa-router'
    import fastapi from "../lib/api"
    import {access_token, username, is_login } from "../lib/store";
    import Error from "../components/Error.svelte"

    let error = {detail:[]}
    let password = ''

    function update_pwd(event) {
        event.preventDefault()
        let url = "/api/user/changepwd"
        let params = {
            password: password
        }        
        
        fastapi('put', url, params, 
            (json) => {
                $access_token = "";
                $username = "";
                $is_login = false;
                push('/user-login');
            },
            (json_error) => {
                error = json_error
            }
        )
    }
    
</script>

<div class="container">
    <h5 class="my-3 border-bottom pb-2">비밀번호 변경</h5>
    <Error error={error} />
    <form method="post" class="my-3">
        <div class="mb-3">
            <label for="subject">변경할 비밀번호</label>
            <input type="text" class="form-control" bind:value="{password}">
        </div>
        <button class="btn btn-primary" 
            on:click="{update_pwd}">
            수정하기
        </button>
    </form>
</div>