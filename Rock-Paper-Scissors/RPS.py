def player(prev_play, opponent_history=[]):
  if not prev_play:
    opponent_history.clear()
  else:
    opponent_history.append(prev_play)
  
  rule = {'R': 'P',
          'P': 'S',
          'S': 'R'}
  
  guess = "S"

  if len(opponent_history) >= 4:
    base = [''.join(opponent_history[i:i+4]) for i, j in enumerate(opponent_history[:-3])]

    potential = [''.join([*opponent_history[-3:], i]) for i in rule.keys()]

    count_base = {k: base.count(k) for k in potential}

    prediction = max(count_base, key=count_base.get)[-1]

    guess = rule[prediction]

  return guess