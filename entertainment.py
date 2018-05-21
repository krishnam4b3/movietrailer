import media
import fresh_tomatoes
Naperu_surya = media.movie("Naperu surya",
                           "Surya is an Indian Army officer who\
                           has serious anger management issues.",
                           "https://bit.ly/2LewXWa",
                           "https://www.youtube.com/watch?v=ZnVIUr_BQSs&t=10s")
Ranga_sthalam = media.movie("Rangasthalam",
                            "Chitti Babu, a hearing impaired boat skipper,\
                            becomes caught in the middle of a political\
                            feud in the village of Rangasthalam.",
                            "https://bit.ly/2kadxWm",
                            "https://www.youtube.com/watch?v=mhhb6JAJKbE")
Avengers_infinitywar = media.movie("Avengers infinity war",
                                   "Iron Man, Thor, the Hulk and the rest of the Avengers\
                                   unite to battle their most powerful\
                                   enemy yet -- the evil Thanos.",
                                   "https://bit.ly/2IvD36S",
                                   "https://www.youtube.com/watc\
                                   h?v=6ZfuNTqbHE8")
Dead_pool2 = media.movie("Deadpool 2",
                         "Wisecracking mercenary Deadpool\
                         joins forces with three\
                          mutants -- Bedlam, Shatterstar\
                          and Domino -- to protect\
                          a boy from the all-powerful Cable.",
                         "https://bit.ly/2Im3MOW",
                         "https://www.youtube.com/wat\
                         ch?v=D86RtevtfrA")
Padmaa_vat = media.movie("Padmaavat",
                         "Set in 1303 AD medieval India,\
                         Padmaavat is the story of honor, valor and obsession.\
                          Queen Padmavati is known for her exceptional\
                          beauty along with a strong sense of justice\
                          and is the wife of\
                          Maharawal Ratan Singh and\
                          pride of the Kingdom of Chittor,\
                           a prosperous kingdom\
                           in the north west of India.",
                         "https://bit.ly/2LkTWii",
                         "https://www.youtube.com/watch?v=X_5_BLt76c0&t=5s")
Tiger_zindahai = media.movie("Tiger zinda hai",
                             "RAW Agent Tiger joins forces with Zoya,\
                             a Pakistani spy, in order\
                             to rescue a group of nurses\
                              who are held hostage by\
                              a terrorist organisation.",
                             "https://bit.ly/2s3xkez",
                             "https://www.youtube.com/watch?v=ePO5M5DE01I")
movies = [Naperu_surya, Ranga_sthalam,
          Avengers_infinitywar, Dead_pool2, Padmaa_vat, Tiger_zindahai]
fresh_tomatoes.open_movies_page(movies)
