<script>
    import fastapi from "../lib/api";
    import { username } from "../lib/store";
    import { link } from "svelte-spa-router";
    import QuestionCreate from "./QuestionCreate.svelte";
    import QuestionModify from "./QuestionModify.svelte";

    let my_questions;

    function get_my_question() {
        fastapi("get", "/api/question/soql/" + username,  {}, (json) => {
            my_questions = json;
            my_questions = [{id:606,subject:"test"}]
        });
    }
    // get_my_question();

</script>

<div class="container">
    <div class="mb-3">
        <h1 class='text-center'>{$username}'s Profile</h1>
    </div>
    <table class="table">
        <thead>
            <tr class="text-center table-dark">
                <th> My Question </th>
                
            </tr>
        </thead>
        <!-- <tbody>
            {#each my_questions as my_question}
                <tr class="text-center">
                    <td class="text-center text-start">
                        <a use:link href="/soql/{username}">
                            {my_question.subject}
                        </a>
                    </td>
                </tr>
            {/each} -->
        <!-- </tbody> -->
    </table>
</div>


<!-- {#each my_question as q} -->
<!-- {/each} -->