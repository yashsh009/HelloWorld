name=input('Are you a human?: ' )
match name:
    case 'indeed' | 'yes' | 'precisely' | 'affirmative' | 'yep':
        print('ok good')
    case 'no' | 'not at all' | 'nah' | 'nope' |'negative':
        print('hmm... interesting')
    case _:
        print('maybe try using a simpler word, can you?')