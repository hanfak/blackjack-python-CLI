US0a
  - User dealt two cards closest to 20 wins
    - from list of cards 1 - 10
  - USer dealt cards including face cards
  - User dealt cards including ace closest to 21
  - List includes suit (and value)
  - Extract cards, hand, card,
  - Two players play(below)

  game.new(hand1, hand2)
  game.deal
    hand1.store(cards.new.randomCard)
    hand2.store(cards.new.randomCard)
    Twice
    game.winner
  game.winner
    hand1.score compare with hand2.score

User story 1:
  - Dealt two cards each
  - Player closest to 21 wins
  - Over 21 loses
  - Under 21 and less than oppenant loses
  - See all cards
  - Shows the score given
  - ace = 11
  - if equal score, draw
  - play new game

User Story 2:
  - If under 21 can hit (Get one card) or stick (no cards)
  - Hit once
  - Both players cards shown
  - if ace, = 11 if sum < 11 else =1
  - if player 1 is bust, player 2 wins automatically, no hits
  - player 2 automatically hits if under 17 and sticks over 16
  - if player 2 is over 21, he loses

User Story 3:
  - Can get multiple hits or choose to stand
  - if 5 cards and 21 or under - wins
  - if go over 21 loses
  - If ace involved, turns to one when sum is greater than 21
  - If hit and over 21, loses
  - If hit and 21, wins

User Story 4: play by rules
  - dealer card not shown
  - player must hit on less than 16
