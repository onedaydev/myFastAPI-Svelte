<script>
    import fastapi from "../lib/api";
    import { access_token, is_login, username } from "../lib/store";
    import { link, push } from "svelte-spa-router";

    let my_questions = [];
    function get_my_question() {
        fastapi("get", "/api/question/soql/" + $username, {}, (json) => {
            my_questions = json.question_list;
        });
    }
    $: get_my_question();

    function delete_user() {
        fastapi("delete", "/api/user/delete", {}, (json) => {
            $access_token = "";
            $username = "";
            $is_login = false;
            push("/");
        });
    }


</script>

<div class="container">
    <div class="mb-3">
        <h1 class="text-center">{$username}'s Profile</h1>
    </div>
    <table class="table">
        <thead>
            <tr class="text-center table-dark">
                <th> My Question & Answer</th>
            </tr>
        </thead>
        <tbody>
            {#each my_questions as my_question}
                <tr class="text-center">
                    <td class="text-center text-start">
                        <a use:link href="/detail/{my_question.id}">
                            {my_question.subject}
                        </a>
                    </td>
                </tr>
            {/each}
        </tbody>
    </table>

    <a
        use:link
        href="/pwdmodify"
        class="btn btn-sm btn-outline-secondary">
        비밀번호 변경
    </a>

    <button
        class="btn btn-sm btn-outline-secondary"
        on:click="{delete_user}">
        회원 탈퇴
    </button>
</div>
