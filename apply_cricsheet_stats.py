import sqlite3

all_stats = {
    "AB de Villiers": {
        "matches": 170,
        "runs": 5181,
        "wickets": 0,
        "batting_avg": 39.85,
        "bowling_avg": 0.0,
        "strike_rate": 151.89,
        "economy": 0.0
    },
    "Aakash Chopra": {
        "matches": 6,
        "runs": 53,
        "wickets": 0,
        "batting_avg": 8.83,
        "bowling_avg": 0.0,
        "strike_rate": 74.65,
        "economy": 0.0
    },
    "Abdul Samad": {
        "matches": 56,
        "runs": 815,
        "wickets": 2,
        "batting_avg": 18.52,
        "bowling_avg": 62.5,
        "strike_rate": 146.85,
        "economy": 13.16
    },
    "Abhinav Manohar": {
        "matches": 20,
        "runs": 292,
        "wickets": 0,
        "batting_avg": 15.37,
        "bowling_avg": 0.0,
        "strike_rate": 124.26,
        "economy": 0.0
    },
    "Abhinav Mukund": {
        "matches": 2,
        "runs": 19,
        "wickets": 0,
        "batting_avg": 9.5,
        "bowling_avg": 0.0,
        "strike_rate": 86.36,
        "economy": 0.0
    },
    "Abhishek Sharma": {
        "matches": 86,
        "runs": 2241,
        "wickets": 11,
        "batting_avg": 29.88,
        "bowling_avg": 48.73,
        "strike_rate": 170.16,
        "economy": 9.11
    },
    "Abishek Porel": {
        "matches": 30,
        "runs": 691,
        "wickets": 0,
        "batting_avg": 25.59,
        "bowling_avg": 0.0,
        "strike_rate": 145.78,
        "economy": 0.0
    },
    "Adam Zampa": {
        "matches": 22,
        "runs": 15,
        "wickets": 31,
        "batting_avg": 3.0,
        "bowling_avg": 21.03,
        "strike_rate": 62.5,
        "economy": 8.38
    },
    "Akash Deep": {
        "matches": 14,
        "runs": 25,
        "wickets": 10,
        "batting_avg": 8.33,
        "bowling_avg": 54.8,
        "strike_rate": 178.57,
        "economy": 11.83
    },
    "Akash Madhwal": {
        "matches": 17,
        "runs": 8,
        "wickets": 23,
        "batting_avg": 8.0,
        "bowling_avg": 25.65,
        "strike_rate": 57.14,
        "economy": 10.06
    },
    "Amit Mishra": {
        "matches": 162,
        "runs": 381,
        "wickets": 174,
        "batting_avg": 11.91,
        "bowling_avg": 23.82,
        "strike_rate": 90.93,
        "economy": 7.38
    },
    "Angkrish Raghuvanshi": {
        "matches": 26,
        "runs": 672,
        "wickets": 0,
        "batting_avg": 29.22,
        "bowling_avg": 0.0,
        "strike_rate": 143.59,
        "economy": 0.0
    },
    "Anil Kumble": {
        "matches": 42,
        "runs": 35,
        "wickets": 45,
        "batting_avg": 11.67,
        "bowling_avg": 23.51,
        "strike_rate": 74.47,
        "economy": 6.58
    },
    "Ankit Sharma": {
        "matches": 21,
        "runs": 87,
        "wickets": 12,
        "batting_avg": 12.43,
        "bowling_avg": 37.5,
        "strike_rate": 129.85,
        "economy": 7.36
    },
    "Anmolpreet Singh": {
        "matches": 9,
        "runs": 139,
        "wickets": 0,
        "batting_avg": 15.44,
        "bowling_avg": 0.0,
        "strike_rate": 120.87,
        "economy": 0.0
    },
    "Anrich Nortje": {
        "matches": 49,
        "runs": 49,
        "wickets": 61,
        "batting_avg": 7.0,
        "bowling_avg": 27.8,
        "strike_rate": 98.0,
        "economy": 9.09
    },
    "Anuj Rawat": {
        "matches": 21,
        "runs": 318,
        "wickets": 0,
        "batting_avg": 19.88,
        "bowling_avg": 0.0,
        "strike_rate": 119.1,
        "economy": 0.0
    },
    "Anureet Singh": {
        "matches": 22,
        "runs": 36,
        "wickets": 18,
        "batting_avg": 9.0,
        "bowling_avg": 34.61,
        "strike_rate": 76.6,
        "economy": 9.07
    },
    "Arjun Tendulkar": {
        "matches": 5,
        "runs": 13,
        "wickets": 3,
        "batting_avg": 13.0,
        "bowling_avg": 38.0,
        "strike_rate": 144.44,
        "economy": 9.37
    },
    "Arshad Khan": {
        "matches": 20,
        "runs": 119,
        "wickets": 17,
        "batting_avg": 23.8,
        "bowling_avg": 33.06,
        "strike_rate": 141.67,
        "economy": 11.09
    },
    "Arshdeep Singh": {
        "matches": 89,
        "runs": 31,
        "wickets": 105,
        "batting_avg": 5.17,
        "bowling_avg": 27.61,
        "strike_rate": 67.39,
        "economy": 9.18
    },
    "Ashish Nehra": {
        "matches": 88,
        "runs": 41,
        "wickets": 106,
        "batting_avg": 5.86,
        "bowling_avg": 23.54,
        "strike_rate": 66.13,
        "economy": 7.85
    },
    "Ashutosh Sharma": {
        "matches": 21,
        "runs": 451,
        "wickets": 0,
        "batting_avg": 28.19,
        "bowling_avg": 0.0,
        "strike_rate": 164.0,
        "economy": 0.0
    },
    "Atharva Taide": {
        "matches": 10,
        "runs": 260,
        "wickets": 0,
        "batting_avg": 26.0,
        "bowling_avg": 0.0,
        "strike_rate": 146.89,
        "economy": 24.0
    },
    "Avesh Khan": {
        "matches": 80,
        "runs": 68,
        "wickets": 92,
        "batting_avg": 17.0,
        "bowling_avg": 28.63,
        "strike_rate": 158.14,
        "economy": 9.18
    },
    "Ayush Badoni": {
        "matches": 56,
        "runs": 1135,
        "wickets": 4,
        "batting_avg": 25.8,
        "bowling_avg": 15.75,
        "strike_rate": 138.92,
        "economy": 9.22
    },
    "Azmatullah Omarzai": {
        "matches": 15,
        "runs": 99,
        "wickets": 12,
        "batting_avg": 12.38,
        "bowling_avg": 38.75,
        "strike_rate": 133.78,
        "economy": 9.69
    },
    "BR Sharath": {
        "matches": 1,
        "runs": 2,
        "wickets": 0,
        "batting_avg": 2.0,
        "bowling_avg": 0.0,
        "strike_rate": 40.0,
        "economy": 0.0
    },
    "Baba Indrajith": {
        "matches": 3,
        "runs": 21,
        "wickets": 0,
        "batting_avg": 7.0,
        "bowling_avg": 0.0,
        "strike_rate": 70.0,
        "economy": 0.0
    },
    "Basil Thampi": {
        "matches": 25,
        "runs": 32,
        "wickets": 22,
        "batting_avg": 32.0,
        "bowling_avg": 38.45,
        "strike_rate": 91.43,
        "economy": 9.74
    },
    "Bhuvneshwar Kumar": {
        "matches": 199,
        "runs": 347,
        "wickets": 215,
        "batting_avg": 9.13,
        "bowling_avg": 26.4,
        "strike_rate": 92.53,
        "economy": 7.68
    },
    "Bipul Sharma": {
        "matches": 29,
        "runs": 187,
        "wickets": 17,
        "batting_avg": 23.38,
        "bowling_avg": 33.65,
        "strike_rate": 152.03,
        "economy": 8.06
    },
    "CM Gautam": {
        "matches": 13,
        "runs": 169,
        "wickets": 0,
        "batting_avg": 16.9,
        "bowling_avg": 0.0,
        "strike_rate": 112.67,
        "economy": 0.0
    },
    "Cameron Green": {
        "matches": 37,
        "runs": 903,
        "wickets": 18,
        "batting_avg": 37.62,
        "bowling_avg": 42.28,
        "strike_rate": 153.57,
        "economy": 9.38
    },
    "Chetan Sakariya": {
        "matches": 20,
        "runs": 20,
        "wickets": 20,
        "batting_avg": 3.33,
        "bowling_avg": 31.9,
        "strike_rate": 64.52,
        "economy": 8.62
    },
    "Colin Munro": {
        "matches": 12,
        "runs": 177,
        "wickets": 0,
        "batting_avg": 14.75,
        "bowling_avg": 0.0,
        "strike_rate": 125.53,
        "economy": 7.5
    },
    "Devdutt Padikkal": {
        "matches": 82,
        "runs": 2088,
        "wickets": 0,
        "batting_avg": 26.77,
        "bowling_avg": 0.0,
        "strike_rate": 132.15,
        "economy": 0.0
    },
    "Dewald Brevis": {
        "matches": 20,
        "runs": 519,
        "wickets": 1,
        "batting_avg": 25.95,
        "bowling_avg": 8.0,
        "strike_rate": 148.29,
        "economy": 16.0
    },
    "Dhruv Jurel": {
        "matches": 45,
        "runs": 970,
        "wickets": 0,
        "batting_avg": 29.39,
        "bowling_avg": 0.0,
        "strike_rate": 153.0,
        "economy": 0.0
    },
    "Dilshan Madushanka": {
        "matches": 1,
        "runs": 0,
        "wickets": 1,
        "batting_avg": 0.0,
        "bowling_avg": 36.0,
        "strike_rate": 0.0,
        "economy": 9.0
    },
    "Donovan Ferreira": {
        "matches": 10,
        "runs": 238,
        "wickets": 1,
        "batting_avg": 29.75,
        "bowling_avg": 14.0,
        "strike_rate": 166.43,
        "economy": 14.0
    },
    "Duan Jansen": {
        "matches": 1,
        "runs": 0,
        "wickets": 1,
        "batting_avg": 0.0,
        "bowling_avg": 53.0,
        "strike_rate": 0.0,
        "economy": 13.25
    },
    "Evin Lewis": {
        "matches": 26,
        "runs": 654,
        "wickets": 0,
        "batting_avg": 27.25,
        "bowling_avg": 0.0,
        "strike_rate": 137.11,
        "economy": 0.0
    },
    "Fazalhaq Farooqi": {
        "matches": 12,
        "runs": 5,
        "wickets": 6,
        "batting_avg": 5.0,
        "bowling_avg": 72.83,
        "strike_rate": 33.33,
        "economy": 10.32
    },
    "Gautam Gambhir": {
        "matches": 151,
        "runs": 4217,
        "wickets": 0,
        "batting_avg": 31.01,
        "bowling_avg": 0.0,
        "strike_rate": 123.88,
        "economy": 0.0
    },
    "Gerald Coetzee": {
        "matches": 14,
        "runs": 31,
        "wickets": 15,
        "batting_avg": 5.17,
        "bowling_avg": 31.47,
        "strike_rate": 93.94,
        "economy": 10.37
    },
    "Gulbadin Naib": {
        "matches": 2,
        "runs": 19,
        "wickets": 0,
        "batting_avg": 19.0,
        "bowling_avg": 0.0,
        "strike_rate": 126.67,
        "economy": 12.0
    },
    "Harbhajan Singh": {
        "matches": 163,
        "runs": 833,
        "wickets": 150,
        "batting_avg": 15.15,
        "bowling_avg": 26.87,
        "strike_rate": 137.91,
        "economy": 7.08
    },
    "Harpreet Brar": {
        "matches": 47,
        "runs": 244,
        "wickets": 35,
        "batting_avg": 20.33,
        "bowling_avg": 31.71,
        "strike_rate": 120.2,
        "economy": 7.98
    },
    "Harshit Rana": {
        "matches": 32,
        "runs": 59,
        "wickets": 40,
        "batting_avg": 9.83,
        "bowling_avg": 25.73,
        "strike_rate": 105.36,
        "economy": 9.51
    },
    "Heinrich Klaasen": {
        "matches": 54,
        "runs": 1894,
        "wickets": 0,
        "batting_avg": 43.05,
        "bowling_avg": 0.0,
        "strike_rate": 166.87,
        "economy": 0.0
    },
    "Imran Tahir": {
        "matches": 59,
        "runs": 33,
        "wickets": 82,
        "batting_avg": 8.25,
        "bowling_avg": 20.77,
        "strike_rate": 89.19,
        "economy": 7.76
    },
    "Iqbal Abdulla": {
        "matches": 48,
        "runs": 88,
        "wickets": 40,
        "batting_avg": 44.0,
        "bowling_avg": 27.73,
        "strike_rate": 104.76,
        "economy": 7.23
    },
    "Ishan Kishan": {
        "matches": 121,
        "runs": 3310,
        "wickets": 0,
        "batting_avg": 29.55,
        "bowling_avg": 0.0,
        "strike_rate": 141.7,
        "economy": 24.0
    },
    "Ishant Sharma": {
        "matches": 117,
        "runs": 57,
        "wickets": 96,
        "batting_avg": 9.5,
        "bowling_avg": 35.18,
        "strike_rate": 82.61,
        "economy": 8.38
    },
    "Jake Fraser-McGurk": {
        "matches": 15,
        "runs": 385,
        "wickets": 0,
        "batting_avg": 25.67,
        "bowling_avg": 0.0,
        "strike_rate": 199.48,
        "economy": 0.0
    },
    "Joginder Sharma": {
        "matches": 16,
        "runs": 36,
        "wickets": 12,
        "batting_avg": 9.0,
        "bowling_avg": 34.92,
        "strike_rate": 120.0,
        "economy": 9.82
    },
    "KL Rahul": {
        "matches": 144,
        "runs": 5668,
        "wickets": 0,
        "batting_avg": 46.08,
        "bowling_avg": 0.0,
        "strike_rate": 138.89,
        "economy": 0.0
    },
    "Kagiso Rabada": {
        "matches": 93,
        "runs": 250,
        "wickets": 136,
        "batting_avg": 13.16,
        "bowling_avg": 22.64,
        "strike_rate": 108.23,
        "economy": 8.71
    },
    "Kartik Tyagi": {
        "matches": 27,
        "runs": 24,
        "wickets": 24,
        "batting_avg": 4.0,
        "bowling_avg": 40.54,
        "strike_rate": 96.0,
        "economy": 10.0
    },
    "Kuldeep Yadav": {
        "matches": 107,
        "runs": 210,
        "wickets": 109,
        "batting_avg": 11.67,
        "bowling_avg": 28.03,
        "strike_rate": 83.0,
        "economy": 8.23
    },
    "Kumar Kartikeya": {
        "matches": 16,
        "runs": 12,
        "wickets": 12,
        "batting_avg": 3.0,
        "bowling_avg": 33.92,
        "strike_rate": 70.59,
        "economy": 8.66
    },
    "Kumar Kushagra": {
        "matches": 4,
        "runs": 21,
        "wickets": 0,
        "batting_avg": 5.25,
        "bowling_avg": 0.0,
        "strike_rate": 100.0,
        "economy": 0.0
    },
    "Lalit Yadav": {
        "matches": 25,
        "runs": 305,
        "wickets": 10,
        "batting_avg": 19.06,
        "bowling_avg": 42.5,
        "strike_rate": 105.17,
        "economy": 8.85
    },
    "Luke Wood": {
        "matches": 2,
        "runs": 9,
        "wickets": 1,
        "batting_avg": 9.0,
        "bowling_avg": 93.0,
        "strike_rate": 300.0,
        "economy": 15.5
    },
    "Lungi Ngidi": {
        "matches": 22,
        "runs": 3,
        "wickets": 36,
        "batting_avg": 1.5,
        "bowling_avg": 20.42,
        "strike_rate": 37.5,
        "economy": 8.58
    },
    "MS Dhoni": {
        "matches": 241,
        "runs": 5439,
        "wickets": 0,
        "batting_avg": 38.3,
        "bowling_avg": 0.0,
        "strike_rate": 137.45,
        "economy": 0.0
    },
    "Maheesh Theekshana": {
        "matches": 38,
        "runs": 17,
        "wickets": 36,
        "batting_avg": 5.67,
        "bowling_avg": 33.53,
        "strike_rate": 50.0,
        "economy": 8.27
    },
    "Manan Vohra": {
        "matches": 51,
        "runs": 1083,
        "wickets": 0,
        "batting_avg": 22.1,
        "bowling_avg": 0.0,
        "strike_rate": 130.64,
        "economy": 0.0
    },
    "Mandeep Singh": {
        "matches": 97,
        "runs": 1706,
        "wickets": 0,
        "batting_avg": 20.8,
        "bowling_avg": 0.0,
        "strike_rate": 122.91,
        "economy": 13.0
    },
    "Marco Jansen": {
        "matches": 42,
        "runs": 151,
        "wickets": 41,
        "batting_avg": 12.58,
        "bowling_avg": 34.27,
        "strike_rate": 107.86,
        "economy": 9.4
    },
    "Matheesha Pathirana": {
        "matches": 32,
        "runs": 0,
        "wickets": 47,
        "batting_avg": 0.0,
        "bowling_avg": 21.62,
        "strike_rate": 0.0,
        "economy": 8.68
    },
    "Mayank Dagar": {
        "matches": 8,
        "runs": 0,
        "wickets": 2,
        "batting_avg": 0.0,
        "bowling_avg": 101.5,
        "strike_rate": 0.0,
        "economy": 8.89
    },
    "Mayank Markande": {
        "matches": 40,
        "runs": 48,
        "wickets": 37,
        "batting_avg": 16.0,
        "bowling_avg": 30.95,
        "strike_rate": 114.29,
        "economy": 9.16
    },
    "Mohammad Kaif": {
        "matches": 22,
        "runs": 259,
        "wickets": 0,
        "batting_avg": 14.39,
        "bowling_avg": 0.0,
        "strike_rate": 103.6,
        "economy": 0.0
    },
    "Mohammad Nabi": {
        "matches": 24,
        "runs": 221,
        "wickets": 15,
        "batting_avg": 13.0,
        "bowling_avg": 34.47,
        "strike_rate": 145.39,
        "economy": 7.44
    },
    "Mohammed Shami": {
        "matches": 127,
        "runs": 115,
        "wickets": 140,
        "batting_avg": 6.39,
        "bowling_avg": 28.62,
        "strike_rate": 104.55,
        "economy": 8.59
    },
    "Mohammed Siraj": {
        "matches": 117,
        "runs": 112,
        "wickets": 118,
        "batting_avg": 10.18,
        "bowling_avg": 30.65,
        "strike_rate": 88.89,
        "economy": 8.69
    },
    "Mohsin Khan": {
        "matches": 27,
        "runs": 25,
        "wickets": 36,
        "batting_avg": 5.0,
        "bowling_avg": 21.97,
        "strike_rate": 89.29,
        "economy": 8.15
    },
    "Morne Morkel": {
        "matches": 70,
        "runs": 126,
        "wickets": 77,
        "batting_avg": 11.45,
        "bowling_avg": 27.13,
        "strike_rate": 140.0,
        "economy": 7.69
    },
    "Mujeeb Ur Rahman": {
        "matches": 20,
        "runs": 12,
        "wickets": 20,
        "batting_avg": 4.0,
        "bowling_avg": 31.0,
        "strike_rate": 80.0,
        "economy": 8.34
    },
    "Mukesh Kumar": {
        "matches": 39,
        "runs": 10,
        "wickets": 41,
        "batting_avg": 10.0,
        "bowling_avg": 33.59,
        "strike_rate": 55.56,
        "economy": 10.51
    },
    "Murugan Ashwin": {
        "matches": 44,
        "runs": 35,
        "wickets": 35,
        "batting_avg": 3.89,
        "bowling_avg": 33.2,
        "strike_rate": 70.0,
        "economy": 8.01
    },
    "Mustafizur Rahman": {
        "matches": 60,
        "runs": 13,
        "wickets": 65,
        "batting_avg": 6.5,
        "bowling_avg": 28.45,
        "strike_rate": 54.17,
        "economy": 8.13
    },
    "Muttiah Muralitharan": {
        "matches": 66,
        "runs": 20,
        "wickets": 64,
        "batting_avg": 3.33,
        "bowling_avg": 26.66,
        "strike_rate": 66.67,
        "economy": 6.7
    },
    "Naman Dhir": {
        "matches": 27,
        "runs": 568,
        "wickets": 0,
        "batting_avg": 27.05,
        "bowling_avg": 0.0,
        "strike_rate": 168.05,
        "economy": 8.77
    },
    "Nandre Burger": {
        "matches": 15,
        "runs": 3,
        "wickets": 16,
        "batting_avg": 3.0,
        "bowling_avg": 30.06,
        "strike_rate": 60.0,
        "economy": 9.72
    },
    "Narayan Jagadeesan": {
        "matches": 10,
        "runs": 162,
        "wickets": 0,
        "batting_avg": 18.0,
        "bowling_avg": 0.0,
        "strike_rate": 110.2,
        "economy": 0.0
    },
    "Navdeep Saini": {
        "matches": 32,
        "runs": 33,
        "wickets": 24,
        "batting_avg": 8.25,
        "bowling_avg": 40.96,
        "strike_rate": 89.19,
        "economy": 8.8
    },
    "Naveen-ul-Haq": {
        "matches": 17,
        "runs": 18,
        "wickets": 25,
        "batting_avg": 18.0,
        "bowling_avg": 23.64,
        "strike_rate": 72.0,
        "economy": 9.16
    },
    "Nehal Wadhera": {
        "matches": 36,
        "runs": 784,
        "wickets": 0,
        "batting_avg": 24.5,
        "bowling_avg": 0.0,
        "strike_rate": 141.52,
        "economy": 7.76
    },
    "Nicholas Pooran": {
        "matches": 94,
        "runs": 2375,
        "wickets": 0,
        "batting_avg": 30.45,
        "bowling_avg": 0.0,
        "strike_rate": 162.56,
        "economy": 0.0
    },
    "Nitish Rana": {
        "matches": 121,
        "runs": 3055,
        "wickets": 10,
        "batting_avg": 27.77,
        "bowling_avg": 32.5,
        "strike_rate": 138.11,
        "economy": 9.03
    },
    "Noor Ahmad": {
        "matches": 45,
        "runs": 30,
        "wickets": 55,
        "batting_avg": 3.0,
        "bowling_avg": 24.02,
        "strike_rate": 56.6,
        "economy": 8.2
    },
    "Nuwan Thushara": {
        "matches": 8,
        "runs": 0,
        "wickets": 9,
        "batting_avg": 0.0,
        "bowling_avg": 31.44,
        "strike_rate": 0.0,
        "economy": 9.43
    },
    "Pawan Negi": {
        "matches": 46,
        "runs": 365,
        "wickets": 34,
        "batting_avg": 14.04,
        "bowling_avg": 27.62,
        "strike_rate": 126.3,
        "economy": 7.87
    },
    "Praveen Kumar": {
        "matches": 119,
        "runs": 340,
        "wickets": 90,
        "batting_avg": 8.95,
        "bowling_avg": 36.12,
        "strike_rate": 108.28,
        "economy": 7.73
    },
    "Pravin Dubey": {
        "matches": 5,
        "runs": 23,
        "wickets": 2,
        "batting_avg": 23.0,
        "bowling_avg": 55.5,
        "strike_rate": 69.7,
        "economy": 8.54
    },
    "R. Sai Kishore": {
        "matches": 25,
        "runs": 18,
        "wickets": 32,
        "batting_avg": 4.5,
        "bowling_avg": 20.34,
        "strike_rate": 112.5,
        "economy": 8.86
    },
    "RP Singh": {
        "matches": 82,
        "runs": 52,
        "wickets": 90,
        "batting_avg": 3.47,
        "bowling_avg": 25.98,
        "strike_rate": 68.42,
        "economy": 7.9
    },
    "Rachin Ravindra": {
        "matches": 18,
        "runs": 413,
        "wickets": 0,
        "batting_avg": 24.29,
        "bowling_avg": 0.0,
        "strike_rate": 143.9,
        "economy": 3.5
    },
    "Rahmanullah Gurbaz": {
        "matches": 18,
        "runs": 363,
        "wickets": 0,
        "batting_avg": 21.35,
        "bowling_avg": 0.0,
        "strike_rate": 134.94,
        "economy": 0.0
    },
    "Rahul Tewatia": {
        "matches": 97,
        "runs": 1188,
        "wickets": 32,
        "batting_avg": 23.76,
        "bowling_avg": 34.72,
        "strike_rate": 136.55,
        "economy": 7.91
    },
    "Rajat Bhatia": {
        "matches": 94,
        "runs": 342,
        "wickets": 71,
        "batting_avg": 11.4,
        "bowling_avg": 28.45,
        "strike_rate": 120.42,
        "economy": 7.41
    },
    "Ramandeep Singh": {
        "matches": 27,
        "runs": 299,
        "wickets": 7,
        "batting_avg": 18.69,
        "bowling_avg": 13.43,
        "strike_rate": 145.85,
        "economy": 10.07
    },
    "Rashid Khan": {
        "matches": 145,
        "runs": 620,
        "wickets": 168,
        "batting_avg": 14.09,
        "bowling_avg": 24.14,
        "strike_rate": 157.36,
        "economy": 7.16
    },
    "Rasikh Salam": {
        "matches": 18,
        "runs": 40,
        "wickets": 16,
        "batting_avg": 8.0,
        "bowling_avg": 34.06,
        "strike_rate": 100.0,
        "economy": 10.03
    },
    "Ravi Bishnoi": {
        "matches": 85,
        "runs": 45,
        "wickets": 83,
        "batting_avg": 3.75,
        "bowling_avg": 30.05,
        "strike_rate": 65.22,
        "economy": 8.36
    },
    "Ravichandran Ashwin": {
        "matches": 217,
        "runs": 833,
        "wickets": 187,
        "batting_avg": 13.02,
        "bowling_avg": 30.22,
        "strike_rate": 118.16,
        "economy": 7.2
    },
    "Rishi Dhawan": {
        "matches": 37,
        "runs": 210,
        "wickets": 25,
        "batting_avg": 19.09,
        "bowling_avg": 35.64,
        "strike_rate": 112.3,
        "economy": 8.08
    },
    "Riyan Parag": {
        "matches": 85,
        "runs": 1777,
        "wickets": 9,
        "batting_avg": 25.39,
        "bowling_avg": 57.22,
        "strike_rate": 142.16,
        "economy": 9.69
    },
    "Rohit Sharma": {
        "matches": 44,
        "runs": 66,
        "wickets": 40,
        "batting_avg": 4.71,
        "bowling_avg": 27.15,
        "strike_rate": 88.0,
        "economy": 7.02
    },
    "Romario Shepherd": {
        "matches": 26,
        "runs": 241,
        "wickets": 15,
        "batting_avg": 24.1,
        "bowling_avg": 40.8,
        "strike_rate": 189.76,
        "economy": 12.0
    },
    "Rovman Powell": {
        "matches": 28,
        "runs": 486,
        "wickets": 1,
        "batting_avg": 21.13,
        "bowling_avg": 35.0,
        "strike_rate": 143.36,
        "economy": 11.67
    },
    "Sachin Baby": {
        "matches": 13,
        "runs": 144,
        "wickets": 2,
        "batting_avg": 16.0,
        "bowling_avg": 4.0,
        "strike_rate": 122.03,
        "economy": 4.8
    },
    "Sameer Rizvi": {
        "matches": 16,
        "runs": 381,
        "wickets": 0,
        "batting_avg": 29.31,
        "bowling_avg": 0.0,
        "strike_rate": 145.42,
        "economy": 0.0
    },
    "Sandeep Sharma": {
        "matches": 141,
        "runs": 60,
        "wickets": 151,
        "batting_avg": 10.0,
        "bowling_avg": 28.24,
        "strike_rate": 80.0,
        "economy": 8.13
    },
    "Sanvir Singh": {
        "matches": 5,
        "runs": 25,
        "wickets": 0,
        "batting_avg": 12.5,
        "bowling_avg": 0.0,
        "strike_rate": 119.05,
        "economy": 0.0
    },
    "Saurav Chauhan": {
        "matches": 3,
        "runs": 18,
        "wickets": 0,
        "batting_avg": 6.0,
        "bowling_avg": 0.0,
        "strike_rate": 120.0,
        "economy": 0.0
    },
    "Shahbaz Ahmed": {
        "matches": 54,
        "runs": 560,
        "wickets": 22,
        "batting_avg": 19.31,
        "bowling_avg": 43.41,
        "strike_rate": 120.69,
        "economy": 9.65
    },
    "Shahbaz Nadeem": {
        "matches": 71,
        "runs": 39,
        "wickets": 48,
        "batting_avg": 2.79,
        "bowling_avg": 37.17,
        "strike_rate": 44.83,
        "economy": 7.56
    },
    "Shakib Al Hasan": {
        "matches": 71,
        "runs": 795,
        "wickets": 63,
        "batting_avg": 19.39,
        "bowling_avg": 29.19,
        "strike_rate": 124.41,
        "economy": 7.44
    },
    "Shamar Joseph": {
        "matches": 1,
        "runs": 0,
        "wickets": 0,
        "batting_avg": 0.0,
        "bowling_avg": 0.0,
        "strike_rate": 0.0,
        "economy": 11.75
    },
    "Shashank Singh": {
        "matches": 40,
        "runs": 843,
        "wickets": 4,
        "batting_avg": 40.14,
        "bowling_avg": 22.75,
        "strike_rate": 160.27,
        "economy": 9.1
    },
    "Shikhar Dhawan": {
        "matches": 221,
        "runs": 6769,
        "wickets": 4,
        "batting_avg": 35.07,
        "bowling_avg": 16.5,
        "strike_rate": 127.09,
        "economy": 8.25
    },
    "Shivam Dube": {
        "matches": 84,
        "runs": 2009,
        "wickets": 6,
        "batting_avg": 30.44,
        "bowling_avg": 41.67,
        "strike_rate": 143.4,
        "economy": 10.56
    },
    "Shivam Mavi": {
        "matches": 32,
        "runs": 51,
        "wickets": 30,
        "batting_avg": 5.67,
        "bowling_avg": 31.4,
        "strike_rate": 91.07,
        "economy": 8.71
    },
    "Shreyas Gopal": {
        "matches": 51,
        "runs": 180,
        "wickets": 52,
        "batting_avg": 12.86,
        "bowling_avg": 25.94,
        "strike_rate": 106.51,
        "economy": 8.17
    },
    "Shubman Gill": {
        "matches": 122,
        "runs": 4239,
        "wickets": 0,
        "batting_avg": 39.99,
        "bowling_avg": 0.0,
        "strike_rate": 140.04,
        "economy": 0.0
    },
    "Siddarth Kaul": {
        "matches": 55,
        "runs": 20,
        "wickets": 58,
        "batting_avg": 5.0,
        "bowling_avg": 29.98,
        "strike_rate": 55.56,
        "economy": 8.63
    },
    "Suyash Sharma": {
        "matches": 35,
        "runs": 0,
        "wickets": 25,
        "batting_avg": 0.0,
        "bowling_avg": 42.48,
        "strike_rate": 0.0,
        "economy": 8.65
    },
    "Swapnil Singh": {
        "matches": 14,
        "runs": 51,
        "wickets": 7,
        "batting_avg": 10.2,
        "bowling_avg": 34.43,
        "strike_rate": 113.33,
        "economy": 8.93
    },
    "T Natarajan": {
        "matches": 72,
        "runs": 4,
        "wickets": 73,
        "batting_avg": 4.0,
        "bowling_avg": 32.04,
        "strike_rate": 57.14,
        "economy": 9.12
    },
    "Tabraiz Shamsi": {
        "matches": 5,
        "runs": 2,
        "wickets": 3,
        "batting_avg": 2.0,
        "bowling_avg": 60.33,
        "strike_rate": 50.0,
        "economy": 9.05
    },
    "Tilak Varma": {
        "matches": 59,
        "runs": 1687,
        "wickets": 0,
        "batting_avg": 35.89,
        "bowling_avg": 0.0,
        "strike_rate": 146.82,
        "economy": 7.64
    },
    "Tristan Stubbs": {
        "matches": 39,
        "runs": 930,
        "wickets": 4,
        "batting_avg": 44.29,
        "bowling_avg": 17.25,
        "strike_rate": 157.63,
        "economy": 11.5
    },
    "Umran Malik": {
        "matches": 26,
        "runs": 23,
        "wickets": 29,
        "batting_avg": 11.5,
        "bowling_avg": 26.62,
        "strike_rate": 143.75,
        "economy": 9.4
    },
    "Urvil Patel": {
        "matches": 4,
        "runs": 72,
        "wickets": 0,
        "batting_avg": 18.0,
        "bowling_avg": 0.0,
        "strike_rate": 205.71,
        "economy": 0.0
    },
    "Vidwath Kaverappa": {
        "matches": 1,
        "runs": 0,
        "wickets": 2,
        "batting_avg": 0.0,
        "bowling_avg": 18.0,
        "strike_rate": 0.0,
        "economy": 9.0
    },
    "Vijay Shankar": {
        "matches": 69,
        "runs": 1233,
        "wickets": 9,
        "batting_avg": 26.23,
        "bowling_avg": 38.22,
        "strike_rate": 129.79,
        "economy": 8.67
    },
    "Virat Kohli": {
        "matches": 269,
        "runs": 9050,
        "wickets": 4,
        "batting_avg": 40.04,
        "bowling_avg": 92.0,
        "strike_rate": 134.03,
        "economy": 8.8
    },
    "Virender Sehwag": {
        "matches": 104,
        "runs": 2728,
        "wickets": 6,
        "batting_avg": 27.56,
        "bowling_avg": 39.17,
        "strike_rate": 155.44,
        "economy": 10.37
    },
    "Vishnu Vinod": {
        "matches": 6,
        "runs": 56,
        "wickets": 0,
        "batting_avg": 9.33,
        "bowling_avg": 0.0,
        "strike_rate": 98.25,
        "economy": 0.0
    },
    "Vivrant Sharma": {
        "matches": 2,
        "runs": 69,
        "wickets": 0,
        "batting_avg": 69.0,
        "bowling_avg": 0.0,
        "strike_rate": 146.81,
        "economy": 12.33
    },
    "Washington Sundar": {
        "matches": 74,
        "runs": 680,
        "wickets": 40,
        "batting_avg": 17.44,
        "bowling_avg": 37.17,
        "strike_rate": 130.02,
        "economy": 7.76
    },
    "Wasim Jaffer": {
        "matches": 8,
        "runs": 130,
        "wickets": 0,
        "batting_avg": 16.25,
        "bowling_avg": 0.0,
        "strike_rate": 107.44,
        "economy": 0.0
    },
    "Yash Thakur": {
        "matches": 21,
        "runs": 0,
        "wickets": 25,
        "batting_avg": 0.0,
        "bowling_avg": 30.8,
        "strike_rate": 0.0,
        "economy": 10.43
    },
    "Yuvraj Singh": {
        "matches": 129,
        "runs": 2754,
        "wickets": 36,
        "batting_avg": 24.81,
        "bowling_avg": 29.92,
        "strike_rate": 129.78,
        "economy": 7.44
    },
    "Zaheer Khan": {
        "matches": 99,
        "runs": 117,
        "wickets": 102,
        "batting_avg": 8.36,
        "bowling_avg": 27.27,
        "strike_rate": 82.98,
        "economy": 7.59
    }
}


def apply_all():
    conn = sqlite3.connect('ipl_auction.db')
    cursor = conn.cursor()
    for name, stats in all_stats.items():
        cursor.execute("""
            UPDATE players 
            SET matches=?, runs=?, wickets=?, batting_avg=?, bowling_avg=?, strike_rate=?, economy=?
            WHERE name=?
        """, (stats['matches'], stats['runs'], stats['wickets'], stats['batting_avg'], stats['bowling_avg'], stats['strike_rate'], stats['economy'], name))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    apply_all()

superstars = {
    "Rohit Sharma": {"matches": 257, "runs": 6628, "wickets": 15, "batting_avg": 29.72, "strike_rate": 131.14},
    "Suryakumar Yadav": {"matches": 150, "runs": 3594, "wickets": 0, "batting_avg": 32.37, "strike_rate": 145.3},
    "Hardik Pandya": {"matches": 137, "runs": 2525, "wickets": 64, "batting_avg": 28.5, "strike_rate": 146.0},
    "Rishabh Pant": {"matches": 111, "runs": 3284, "wickets": 0, "batting_avg": 35.31, "strike_rate": 148.93},
    "Shreyas Iyer": {"matches": 115, "runs": 3127, "wickets": 0, "batting_avg": 32.24, "strike_rate": 127.42},
    "Jasprit Bumrah": {"matches": 133, "runs": 69, "wickets": 165, "batting_avg": 0, "strike_rate": 0},
    "Ravindra Jadeja": {"matches": 240, "runs": 2959, "wickets": 160, "batting_avg": 27.4, "strike_rate": 129.0},
    "KL Rahul": {"matches": 132, "runs": 4683, "wickets": 0, "batting_avg": 45.0, "strike_rate": 134.4},
    "Sanju Samson": {"matches": 167, "runs": 4419, "wickets": 0, "batting_avg": 30.6, "strike_rate": 139.0},
    "Yuzvendra Chahal": {"matches": 160, "runs": 43, "wickets": 205, "batting_avg": 0, "strike_rate": 0},
    "MS Dhoni": {"matches": 264, "runs": 5243, "wickets": 0, "batting_avg": 39.12, "strike_rate": 137.5},
    "Virat Kohli": {"matches": 252, "runs": 8004, "wickets": 4, "batting_avg": 38.6, "strike_rate": 131.9},
    "Andre Russell": {"matches": 127, "runs": 2484, "wickets": 115, "batting_avg": 29.5, "strike_rate": 174.0},
    "Sunil Narine": {"matches": 176, "runs": 1534, "wickets": 180, "batting_avg": 17.0, "strike_rate": 165.8}
}

conn = sqlite3.connect('ipl_auction.db')
cursor = conn.cursor()
for name, stats in superstars.items():
    cursor.execute("""
        UPDATE players 
        SET matches=?, runs=?, wickets=?, batting_avg=?, strike_rate=?
        WHERE name=?
    """, (stats["matches"], stats["runs"], stats["wickets"], stats["batting_avg"], stats["strike_rate"], name))
conn.commit()
conn.close()
