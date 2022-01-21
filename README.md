# LogRNG
Generate a random number with more odds of it being a lower number than a higher one
## Parameters
- power -> If you generate a number from 0 to 10, there will be a X chance of it being between 9 and 10:
  - Power 0 -> X ≈ 10%
  - Power 1 -> X ≈ 1%
  - Power 2 -> X ≈ 0.112734%
  - Power 3 -> X ≈ 0.013167%
  - Power 4 -> ...
...

- decimals -> Decimals of the generated number
- ran -> Range of the random number ( e.g. [0,10] )
