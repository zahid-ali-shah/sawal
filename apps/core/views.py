from django.shortcuts import render


def question_view(request):
    dummy_question = """I once spent 3 months writing literally 5 lines of code in total. Managers loved my performance
    and praised me for months. Was I slacking? No. Was I avoiding writing code? No. Was it fun to only write this
    amount? No. It took very long time to untangle issues we had in system. Once hard work was done, fix was trivial.
    It is a bit like this joke about fixing a machine with a hammer. Old engineer has been called up to misbehaving
    machine that company couldn't fix. He went around few times, hit it with a hammer and machine was fine since.
    He asked for $50k for service, company managers considered this charge excessive and asked for breakdown.
    He delivered invoice: $1 hitting with a hammer, $49.999 knowing where to hit. That’s how most of programming
    looks these days. Hammers are cheap but figuring out what to do with them takes disproportionate amount
    of time. So what is 'browsing internet' in daily job? Is looking through documentation ok? Maybe 
    Stack Overflow answers too? What if I’m looking through libraries on GitHub that will reduce my work from
    month to 2 days, is that not “working”? I hope you see the problem with this judgement."""

    char_limit = 600
    question_less = dummy_question if len(dummy_question) <= char_limit else dummy_question[:char_limit]
    context = {
        "question_less": question_less,
        "question_more": dummy_question[char_limit:]

    }

    return render(request, "core/question.html", context)
