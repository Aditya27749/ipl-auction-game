import sqlite3

all_stats = {
    "Virat Kohli": {
        "matches": 277,
        "runs": 18692,
        "wickets": 8,
        "batting_avg": 40.46,
        "bowling_avg": 92.0,
        "strike_rate": 134.86,
        "economy": 8.8
    },
    "Rohit Sharma": {
        "matches": 45,
        "runs": 132,
        "wickets": 80,
        "batting_avg": 4.71,
        "bowling_avg": 27.15,
        "strike_rate": 88.0,
        "economy": 7.02
    },
    "Shubman Gill": {
        "matches": 131,
        "runs": 9196,
        "wickets": 0,
        "batting_avg": 40.33,
        "bowling_avg": 0.0,
        "strike_rate": 142.09,
        "economy": 0.0
    },
    "KL Rahul": {
        "matches": 150,
        "runs": 11656,
        "wickets": 0,
        "batting_avg": 45.53,
        "bowling_avg": 0.0,
        "strike_rate": 139.16,
        "economy": 0.0
    },
    "Suryakumar Yadav": {
        "matches": 100,
        "runs": 2800,
        "wickets": 0,
        "batting_avg": 32.0,
        "bowling_avg": 0.0,
        "strike_rate": 150.0,
        "economy": 0.0
    },
    "Faf du Plessis": {
        "matches": 120,
        "runs": 3800,
        "wickets": 0,
        "batting_avg": 34.0,
        "bowling_avg": 0.0,
        "strike_rate": 135.0,
        "economy": 0.0
    },
    "David Warner": {
        "matches": 180,
        "runs": 6500,
        "wickets": 0,
        "batting_avg": 42.0,
        "bowling_avg": 0.0,
        "strike_rate": 140.0,
        "economy": 0.0
    },
    "Jos Buttler": {
        "matches": 90,
        "runs": 3200,
        "wickets": 0,
        "batting_avg": 38.0,
        "bowling_avg": 0.0,
        "strike_rate": 150.0,
        "economy": 0.0
    },
    "Quinton de Kock": {
        "matches": 100,
        "runs": 3000,
        "wickets": 0,
        "batting_avg": 32.0,
        "bowling_avg": 0.0,
        "strike_rate": 138.0,
        "economy": 0.0
    },
    "Travis Head": {
        "matches": 20,
        "runs": 600,
        "wickets": 2,
        "batting_avg": 35.0,
        "bowling_avg": 45.0,
        "strike_rate": 165.0,
        "economy": 9.5
    },
    "Jasprit Bumrah": {
        "matches": 130,
        "runs": 80,
        "wickets": 170,
        "batting_avg": 8.0,
        "bowling_avg": 24.0,
        "strike_rate": 100.0,
        "economy": 7.4
    },
    "Mohammed Shami": {
        "matches": 133,
        "runs": 230,
        "wickets": 290,
        "batting_avg": 6.05,
        "bowling_avg": 29.08,
        "strike_rate": 103.6,
        "economy": 8.66
    },
    "Rashid Khan": {
        "matches": 154,
        "runs": 1270,
        "wickets": 358,
        "batting_avg": 13.8,
        "bowling_avg": 24.01,
        "strike_rate": 156.4,
        "economy": 7.28
    },
    "Yuzvendra Chahal": {
        "matches": 150,
        "runs": 35,
        "wickets": 190,
        "batting_avg": 5.0,
        "bowling_avg": 22.0,
        "strike_rate": 60.0,
        "economy": 7.5
    },
    "Trent Boult": {
        "matches": 80,
        "runs": 40,
        "wickets": 100,
        "batting_avg": 6.0,
        "bowling_avg": 25.0,
        "strike_rate": 75.0,
        "economy": 8.0
    },
    "Kagiso Rabada": {
        "matches": 102,
        "runs": 524,
        "wickets": 302,
        "batting_avg": 13.1,
        "bowling_avg": 22.3,
        "strike_rate": 109.62,
        "economy": 8.79
    },
    "Mohammed Siraj": {
        "matches": 126,
        "runs": 234,
        "wickets": 256,
        "batting_avg": 9.75,
        "bowling_avg": 30.55,
        "strike_rate": 84.17,
        "economy": 8.78
    },
    "Arshdeep Singh": {
        "matches": 96,
        "runs": 64,
        "wickets": 222,
        "batting_avg": 5.33,
        "bowling_avg": 28.03,
        "strike_rate": 68.09,
        "economy": 9.19
    },
    "Hardik Pandya": {
        "matches": 120,
        "runs": 2200,
        "wickets": 55,
        "batting_avg": 28.0,
        "bowling_avg": 32.0,
        "strike_rate": 148.0,
        "economy": 8.5
    },
    "Ravindra Jadeja": {
        "matches": 230,
        "runs": 2700,
        "wickets": 160,
        "batting_avg": 28.0,
        "bowling_avg": 30.0,
        "strike_rate": 132.0,
        "economy": 7.6
    },
    "Andre Russell": {
        "matches": 110,
        "runs": 2200,
        "wickets": 90,
        "batting_avg": 28.0,
        "bowling_avg": 25.0,
        "strike_rate": 175.0,
        "economy": 9.0
    },
    "Glenn Maxwell": {
        "matches": 110,
        "runs": 2500,
        "wickets": 30,
        "batting_avg": 25.0,
        "bowling_avg": 35.0,
        "strike_rate": 155.0,
        "economy": 8.0
    },
    "Marcus Stoinis": {
        "matches": 60,
        "runs": 1300,
        "wickets": 20,
        "batting_avg": 28.0,
        "bowling_avg": 30.0,
        "strike_rate": 142.0,
        "economy": 9.0
    },
    "Sam Curran": {
        "matches": 40,
        "runs": 500,
        "wickets": 40,
        "batting_avg": 24.0,
        "bowling_avg": 28.0,
        "strike_rate": 135.0,
        "economy": 8.5
    },
    "Axar Patel": {
        "matches": 90,
        "runs": 1200,
        "wickets": 70,
        "batting_avg": 22.0,
        "bowling_avg": 29.0,
        "strike_rate": 140.0,
        "economy": 7.0
    },
    "Shardul Thakur": {
        "matches": 80,
        "runs": 400,
        "wickets": 65,
        "batting_avg": 15.0,
        "bowling_avg": 28.0,
        "strike_rate": 130.0,
        "economy": 8.8
    },
    "MS Dhoni": {
        "matches": 242,
        "runs": 10878,
        "wickets": 0,
        "batting_avg": 38.3,
        "bowling_avg": 0.0,
        "strike_rate": 137.45,
        "economy": 0.0
    },
    "Rishabh Pant": {
        "matches": 110,
        "runs": 3500,
        "wickets": 0,
        "batting_avg": 35.0,
        "bowling_avg": 0.0,
        "strike_rate": 148.0,
        "economy": 0.0
    },
    "Sanju Samson": {
        "matches": 160,
        "runs": 4200,
        "wickets": 0,
        "batting_avg": 29.0,
        "bowling_avg": 0.0,
        "strike_rate": 138.0,
        "economy": 0.0
    },
    "Ishan Kishan": {
        "matches": 128,
        "runs": 7200,
        "wickets": 0,
        "batting_avg": 30.51,
        "bowling_avg": 0.0,
        "strike_rate": 143.54,
        "economy": 24.0
    },
    "Dinesh Karthik": {
        "matches": 250,
        "runs": 4800,
        "wickets": 0,
        "batting_avg": 26.0,
        "bowling_avg": 0.0,
        "strike_rate": 138.0,
        "economy": 0.0
    },
    "Heinrich Klaasen": {
        "matches": 61,
        "runs": 4208,
        "wickets": 0,
        "batting_avg": 42.08,
        "bowling_avg": 0.0,
        "strike_rate": 166.72,
        "economy": 0.0
    },
    "Devdutt Padikkal": {
        "matches": 90,
        "runs": 4540,
        "wickets": 0,
        "batting_avg": 26.71,
        "bowling_avg": 0.0,
        "strike_rate": 133.14,
        "economy": 0.0
    },
    "Ruturaj Gaikwad": {
        "matches": 60,
        "runs": 2000,
        "wickets": 0,
        "batting_avg": 38.0,
        "bowling_avg": 0.0,
        "strike_rate": 135.0,
        "economy": 0.0
    },
    "Yashasvi Jaiswal": {
        "matches": 45,
        "runs": 1400,
        "wickets": 0,
        "batting_avg": 32.0,
        "bowling_avg": 0.0,
        "strike_rate": 150.0,
        "economy": 0.0
    },
    "Prithvi Shaw": {
        "matches": 75,
        "runs": 1800,
        "wickets": 0,
        "batting_avg": 24.0,
        "bowling_avg": 0.0,
        "strike_rate": 145.0,
        "economy": 0.0
    },
    "Abhishek Sharma": {
        "matches": 93,
        "runs": 4758,
        "wickets": 22,
        "batting_avg": 29.37,
        "bowling_avg": 50.0,
        "strike_rate": 171.27,
        "economy": 9.04
    },
    "Tilak Varma": {
        "matches": 66,
        "runs": 3716,
        "wickets": 0,
        "batting_avg": 35.73,
        "bowling_avg": 0.0,
        "strike_rate": 144.7,
        "economy": 7.64
    },
    "Sai Sudharsan": {
        "matches": 25,
        "runs": 900,
        "wickets": 0,
        "batting_avg": 45.0,
        "bowling_avg": 0.0,
        "strike_rate": 135.0,
        "economy": 0.0
    },
    "Rinku Singh": {
        "matches": 40,
        "runs": 950,
        "wickets": 0,
        "batting_avg": 35.0,
        "bowling_avg": 0.0,
        "strike_rate": 145.0,
        "economy": 0.0
    },
    "Rahul Tripathi": {
        "matches": 95,
        "runs": 2200,
        "wickets": 0,
        "batting_avg": 27.0,
        "bowling_avg": 0.0,
        "strike_rate": 138.0,
        "economy": 0.0
    },
    "Nitish Rana": {
        "matches": 124,
        "runs": 6156,
        "wickets": 20,
        "batting_avg": 27.48,
        "bowling_avg": 32.5,
        "strike_rate": 137.72,
        "economy": 9.03
    },
    "Kuldeep Yadav": {
        "matches": 111,
        "runs": 420,
        "wickets": 224,
        "batting_avg": 11.67,
        "bowling_avg": 28.21,
        "strike_rate": 83.0,
        "economy": 8.29
    },
    "Ravichandran Ashwin": {
        "matches": 218,
        "runs": 1666,
        "wickets": 374,
        "batting_avg": 13.02,
        "bowling_avg": 30.22,
        "strike_rate": 118.16,
        "economy": 7.2
    },
    "Bhuvneshwar Kumar": {
        "matches": 207,
        "runs": 708,
        "wickets": 452,
        "batting_avg": 9.32,
        "bowling_avg": 26.16,
        "strike_rate": 93.9,
        "economy": 7.71
    },
    "Umran Malik": {
        "matches": 27,
        "runs": 46,
        "wickets": 58,
        "batting_avg": 11.5,
        "bowling_avg": 26.62,
        "strike_rate": 143.75,
        "economy": 9.4
    },
    "Avesh Khan": {
        "matches": 83,
        "runs": 136,
        "wickets": 186,
        "batting_avg": 17.0,
        "bowling_avg": 29.4,
        "strike_rate": 158.14,
        "economy": 9.28
    },
    "Harshal Patel": {
        "matches": 90,
        "runs": 250,
        "wickets": 115,
        "batting_avg": 12.0,
        "bowling_avg": 24.0,
        "strike_rate": 120.0,
        "economy": 8.5
    },
    "Mohit Sharma": {
        "matches": 100,
        "runs": 150,
        "wickets": 120,
        "batting_avg": 8.0,
        "bowling_avg": 23.0,
        "strike_rate": 105.0,
        "economy": 8.2
    },
    "Tushar Deshpande": {
        "matches": 25,
        "runs": 25,
        "wickets": 25,
        "batting_avg": 6.0,
        "bowling_avg": 28.0,
        "strike_rate": 90.0,
        "economy": 9.5
    },
    "Sandeep Sharma": {
        "matches": 143,
        "runs": 120,
        "wickets": 302,
        "batting_avg": 10.0,
        "bowling_avg": 28.52,
        "strike_rate": 80.0,
        "economy": 8.17
    },
    "Mukesh Kumar": {
        "matches": 43,
        "runs": 20,
        "wickets": 84,
        "batting_avg": 10.0,
        "bowling_avg": 34.64,
        "strike_rate": 55.56,
        "economy": 10.59
    },
    "Pat Cummins": {
        "matches": 50,
        "runs": 400,
        "wickets": 55,
        "batting_avg": 18.0,
        "bowling_avg": 30.0,
        "strike_rate": 150.0,
        "economy": 8.5
    },
    "Mitchell Starc": {
        "matches": 30,
        "runs": 100,
        "wickets": 35,
        "batting_avg": 12.0,
        "bowling_avg": 21.0,
        "strike_rate": 110.0,
        "economy": 7.5
    },
    "Josh Hazlewood": {
        "matches": 30,
        "runs": 25,
        "wickets": 38,
        "batting_avg": 5.0,
        "bowling_avg": 22.0,
        "strike_rate": 75.0,
        "economy": 8.0
    },
    "Mustafizur Rahman": {
        "matches": 61,
        "runs": 26,
        "wickets": 130,
        "batting_avg": 6.5,
        "bowling_avg": 28.45,
        "strike_rate": 54.17,
        "economy": 8.13
    },
    "Anrich Nortje": {
        "matches": 50,
        "runs": 98,
        "wickets": 122,
        "batting_avg": 7.0,
        "bowling_avg": 27.8,
        "strike_rate": 98.0,
        "economy": 9.09
    },
    "Marco Jansen": {
        "matches": 48,
        "runs": 384,
        "wickets": 90,
        "batting_avg": 12.8,
        "bowling_avg": 36.27,
        "strike_rate": 110.34,
        "economy": 9.63
    },
    "Adam Zampa": {
        "matches": 23,
        "runs": 30,
        "wickets": 62,
        "batting_avg": 3.0,
        "bowling_avg": 21.03,
        "strike_rate": 62.5,
        "economy": 8.38
    },
    "Sunil Narine": {
        "matches": 170,
        "runs": 1500,
        "wickets": 175,
        "batting_avg": 16.0,
        "bowling_avg": 25.0,
        "strike_rate": 165.0,
        "economy": 6.8
    },
    "Venkatesh Iyer": {
        "matches": 40,
        "runs": 1100,
        "wickets": 3,
        "batting_avg": 30.0,
        "bowling_avg": 45.0,
        "strike_rate": 135.0,
        "economy": 8.5
    },
    "Washington Sundar": {
        "matches": 82,
        "runs": 1776,
        "wickets": 80,
        "batting_avg": 20.65,
        "bowling_avg": 38.0,
        "strike_rate": 135.37,
        "economy": 7.77
    },
    "Krunal Pandya": {
        "matches": 115,
        "runs": 1500,
        "wickets": 75,
        "batting_avg": 22.0,
        "bowling_avg": 34.0,
        "strike_rate": 130.0,
        "economy": 7.5
    },
    "Liam Livingstone": {
        "matches": 35,
        "runs": 900,
        "wickets": 10,
        "batting_avg": 28.0,
        "bowling_avg": 38.0,
        "strike_rate": 160.0,
        "economy": 9.0
    },
    "Cameron Green": {
        "matches": 44,
        "runs": 2058,
        "wickets": 46,
        "batting_avg": 38.11,
        "bowling_avg": 39.04,
        "strike_rate": 151.1,
        "economy": 9.44
    },
    "Mitchell Marsh": {
        "matches": 40,
        "runs": 700,
        "wickets": 38,
        "batting_avg": 22.0,
        "bowling_avg": 22.0,
        "strike_rate": 130.0,
        "economy": 8.2
    },
    "Phil Salt": {
        "matches": 15,
        "runs": 400,
        "wickets": 0,
        "batting_avg": 30.0,
        "bowling_avg": 0.0,
        "strike_rate": 150.0,
        "economy": 0.0
    },
    "Abhinav Manohar": {
        "matches": 21,
        "runs": 584,
        "wickets": 0,
        "batting_avg": 15.37,
        "bowling_avg": 0.0,
        "strike_rate": 124.26,
        "economy": 0.0
    },
    "Ayush Badoni": {
        "matches": 59,
        "runs": 2356,
        "wickets": 8,
        "batting_avg": 25.61,
        "bowling_avg": 15.75,
        "strike_rate": 140.91,
        "economy": 9.22
    },
    "Prabhsimran Singh": {
        "matches": 25,
        "runs": 500,
        "wickets": 0,
        "batting_avg": 20.0,
        "bowling_avg": 0.0,
        "strike_rate": 145.0,
        "economy": 0.0
    },
    "Dhruv Jurel": {
        "matches": 52,
        "runs": 2390,
        "wickets": 0,
        "batting_avg": 31.45,
        "bowling_avg": 0.0,
        "strike_rate": 154.19,
        "economy": 0.0
    },
    "Nehal Wadhera": {
        "matches": 38,
        "runs": 1568,
        "wickets": 0,
        "batting_avg": 23.76,
        "bowling_avg": 0.0,
        "strike_rate": 140.0,
        "economy": 7.76
    },
    "Yash Thakur": {
        "matches": 23,
        "runs": 0,
        "wickets": 54,
        "batting_avg": 0.0,
        "bowling_avg": 30.56,
        "strike_rate": 0.0,
        "economy": 10.6
    },
    "Akash Madhwal": {
        "matches": 18,
        "runs": 16,
        "wickets": 46,
        "batting_avg": 16.0,
        "bowling_avg": 25.65,
        "strike_rate": 57.14,
        "economy": 10.06
    },
    "Vaibhav Arora": {
        "matches": 15,
        "runs": 15,
        "wickets": 15,
        "batting_avg": 5.0,
        "bowling_avg": 30.0,
        "strike_rate": 70.0,
        "economy": 9.2
    },
    "Harshit Rana": {
        "matches": 33,
        "runs": 118,
        "wickets": 80,
        "batting_avg": 9.83,
        "bowling_avg": 25.73,
        "strike_rate": 105.36,
        "economy": 9.51
    },
    "Suyash Sharma": {
        "matches": 40,
        "runs": 0,
        "wickets": 54,
        "batting_avg": 0.0,
        "bowling_avg": 44.07,
        "strike_rate": 0.0,
        "economy": 8.89
    },
    "Mayank Dagar": {
        "matches": 9,
        "runs": 0,
        "wickets": 4,
        "batting_avg": 0.0,
        "bowling_avg": 101.5,
        "strike_rate": 0.0,
        "economy": 8.89
    },
    "Ramandeep Singh": {
        "matches": 28,
        "runs": 598,
        "wickets": 14,
        "batting_avg": 18.69,
        "bowling_avg": 13.43,
        "strike_rate": 145.85,
        "economy": 10.07
    },
    "Vivrant Sharma": {
        "matches": 3,
        "runs": 138,
        "wickets": 0,
        "batting_avg": 69.0,
        "bowling_avg": 0.0,
        "strike_rate": 146.81,
        "economy": 12.33
    },
    "Hrithik Shokeen": {
        "matches": 10,
        "runs": 40,
        "wickets": 5,
        "batting_avg": 10.0,
        "bowling_avg": 40.0,
        "strike_rate": 100.0,
        "economy": 8.5
    },
    "Kartik Tyagi": {
        "matches": 34,
        "runs": 48,
        "wickets": 66,
        "batting_avg": 3.43,
        "bowling_avg": 36.7,
        "strike_rate": 92.31,
        "economy": 9.98
    },
    "AB de Villiers": {
        "matches": 171,
        "runs": 10362,
        "wickets": 0,
        "batting_avg": 39.85,
        "bowling_avg": 0.0,
        "strike_rate": 151.89,
        "economy": 0.0
    },
    "Chris Gayle": {
        "matches": 142,
        "runs": 4965,
        "wickets": 18,
        "batting_avg": 39.72,
        "bowling_avg": 34.0,
        "strike_rate": 148.96,
        "economy": 7.9
    },
    "Lasith Malinga": {
        "matches": 122,
        "runs": 88,
        "wickets": 170,
        "batting_avg": 5.5,
        "bowling_avg": 19.8,
        "strike_rate": 95.0,
        "economy": 7.14
    },
    "Suresh Raina": {
        "matches": 205,
        "runs": 5528,
        "wickets": 25,
        "batting_avg": 32.5,
        "bowling_avg": 34.0,
        "strike_rate": 136.7,
        "economy": 7.3
    },
    "Kieron Pollard": {
        "matches": 189,
        "runs": 3412,
        "wickets": 69,
        "batting_avg": 28.67,
        "bowling_avg": 31.6,
        "strike_rate": 147.32,
        "economy": 8.7
    },
    "Shikhar Dhawan": {
        "matches": 222,
        "runs": 13538,
        "wickets": 8,
        "batting_avg": 35.07,
        "bowling_avg": 16.5,
        "strike_rate": 127.09,
        "economy": 8.25
    },
    "Gautam Gambhir": {
        "matches": 152,
        "runs": 8434,
        "wickets": 0,
        "batting_avg": 31.01,
        "bowling_avg": 0.0,
        "strike_rate": 123.88,
        "economy": 0.0
    },
    "Shane Watson": {
        "matches": 145,
        "runs": 3874,
        "wickets": 92,
        "batting_avg": 30.99,
        "bowling_avg": 29.15,
        "strike_rate": 137.91,
        "economy": 7.93
    },
    "Sachin Tendulkar": {
        "matches": 78,
        "runs": 2334,
        "wickets": 0,
        "batting_avg": 34.83,
        "bowling_avg": 0.0,
        "strike_rate": 119.81,
        "economy": 0.0
    },
    "Yuvraj Singh": {
        "matches": 130,
        "runs": 5508,
        "wickets": 72,
        "batting_avg": 24.81,
        "bowling_avg": 29.92,
        "strike_rate": 129.78,
        "economy": 7.44
    },
    "Shreyas Iyer": {
        "matches": 115,
        "runs": 3127,
        "wickets": 0,
        "batting_avg": 32.23,
        "bowling_avg": 0.0,
        "strike_rate": 127.42,
        "economy": 0.0
    },
    "Shivam Dube": {
        "matches": 89,
        "runs": 4258,
        "wickets": 12,
        "batting_avg": 31.31,
        "bowling_avg": 46.17,
        "strike_rate": 145.42,
        "economy": 10.79
    },
    "Jofra Archer": {
        "matches": 40,
        "runs": 195,
        "wickets": 48,
        "batting_avg": 15.0,
        "bowling_avg": 24.39,
        "strike_rate": 157.25,
        "economy": 7.43
    },
    "Nicholas Pooran": {
        "matches": 101,
        "runs": 5054,
        "wickets": 0,
        "batting_avg": 30.45,
        "bowling_avg": 0.0,
        "strike_rate": 163.77,
        "economy": 0.0
    },
    "Tim David": {
        "matches": 38,
        "runs": 659,
        "wickets": 0,
        "batting_avg": 28.65,
        "bowling_avg": 0.0,
        "strike_rate": 172.51,
        "economy": 0.0
    },
    "Matheesha Pathirana": {
        "matches": 34,
        "runs": 0,
        "wickets": 94,
        "batting_avg": 0.0,
        "bowling_avg": 21.81,
        "strike_rate": 0.0,
        "economy": 8.66
    },
    "Rajat Patidar": {
        "matches": 27,
        "runs": 799,
        "wickets": 0,
        "batting_avg": 34.73,
        "bowling_avg": 0.0,
        "strike_rate": 158.53,
        "economy": 0.0
    },
    "Rachin Ravindra": {
        "matches": 19,
        "runs": 826,
        "wickets": 0,
        "batting_avg": 24.29,
        "bowling_avg": 0.0,
        "strike_rate": 143.9,
        "economy": 3.5
    },
    "Tristan Stubbs": {
        "matches": 45,
        "runs": 1972,
        "wickets": 8,
        "batting_avg": 39.44,
        "bowling_avg": 17.25,
        "strike_rate": 151.93,
        "economy": 11.5
    },
    "Gerald Coetzee": {
        "matches": 15,
        "runs": 62,
        "wickets": 30,
        "batting_avg": 5.17,
        "bowling_avg": 31.47,
        "strike_rate": 93.94,
        "economy": 10.37
    },
    "Mayank Yadav": {
        "matches": 3,
        "runs": 0,
        "wickets": 7,
        "batting_avg": 0.0,
        "bowling_avg": 12.14,
        "strike_rate": 0.0,
        "economy": 6.98
    },
    "Jake Fraser-McGurk": {
        "matches": 16,
        "runs": 770,
        "wickets": 0,
        "batting_avg": 25.67,
        "bowling_avg": 0.0,
        "strike_rate": 199.48,
        "economy": 0.0
    },
    "Jason Roy": {
        "matches": 14,
        "runs": 326,
        "wickets": 61,
        "batting_avg": 11.92,
        "bowling_avg": 27.33,
        "strike_rate": 99.38,
        "economy": 7.89
    },
    "Ben Stokes": {
        "matches": 110,
        "runs": 2159,
        "wickets": 78,
        "batting_avg": 20.85,
        "bowling_avg": 25.23,
        "strike_rate": 145.81,
        "economy": 7.03
    },
    "Joe Root": {
        "matches": 30,
        "runs": 3562,
        "wickets": 3,
        "batting_avg": 21.76,
        "bowling_avg": 0.0,
        "strike_rate": 143.79,
        "economy": 0.0
    },
    "Dawid Malan": {
        "matches": 112,
        "runs": 50,
        "wickets": 139,
        "batting_avg": 12.9,
        "bowling_avg": 27.37,
        "strike_rate": 127.22,
        "economy": 9.32
    },
    "Eoin Morgan": {
        "matches": 56,
        "runs": 2250,
        "wickets": 68,
        "batting_avg": 26.68,
        "bowling_avg": 30.22,
        "strike_rate": 128.33,
        "economy": 8.52
    },
    "Alex Hales": {
        "matches": 34,
        "runs": 416,
        "wickets": 113,
        "batting_avg": 7.11,
        "bowling_avg": 24.63,
        "strike_rate": 89.86,
        "economy": 8.16
    },
    "Adil Rashid": {
        "matches": 120,
        "runs": 239,
        "wickets": 23,
        "batting_avg": 5.0,
        "bowling_avg": 26.61,
        "strike_rate": 100.56,
        "economy": 8.1
    },
    "Mark Wood": {
        "matches": 115,
        "runs": 287,
        "wickets": 16,
        "batting_avg": 9.35,
        "bowling_avg": 19.77,
        "strike_rate": 98.62,
        "economy": 8.2
    },
    "Chris Woakes": {
        "matches": 148,
        "runs": 206,
        "wickets": 3,
        "batting_avg": 43.4,
        "bowling_avg": 0.0,
        "strike_rate": 148.99,
        "economy": 0.0
    },
    "Moeen Ali": {
        "matches": 45,
        "runs": 1448,
        "wickets": 67,
        "batting_avg": 31.38,
        "bowling_avg": 21.42,
        "strike_rate": 134.89,
        "economy": 8.92
    },
    "Sam Billings": {
        "matches": 132,
        "runs": 3079,
        "wickets": 0,
        "batting_avg": 37.26,
        "bowling_avg": 0.0,
        "strike_rate": 159.54,
        "economy": 0.0
    },
    "Liam Plunkett": {
        "matches": 148,
        "runs": 481,
        "wickets": 147,
        "batting_avg": 7.51,
        "bowling_avg": 22.12,
        "strike_rate": 118.18,
        "economy": 8.7
    },
    "Tom Curran": {
        "matches": 29,
        "runs": 3975,
        "wickets": 4,
        "batting_avg": 29.99,
        "bowling_avg": 0.0,
        "strike_rate": 136.77,
        "economy": 0.0
    },
    "Reece Topley": {
        "matches": 31,
        "runs": 2982,
        "wickets": 4,
        "batting_avg": 36.52,
        "bowling_avg": 0.0,
        "strike_rate": 143.19,
        "economy": 0.0
    },
    "Jason Holder": {
        "matches": 91,
        "runs": 1688,
        "wickets": 42,
        "batting_avg": 23.23,
        "bowling_avg": 21.13,
        "strike_rate": 150.14,
        "economy": 7.86
    },
    "Akeal Hosein": {
        "matches": 135,
        "runs": 1395,
        "wickets": 3,
        "batting_avg": 31.35,
        "bowling_avg": 0.0,
        "strike_rate": 138.26,
        "economy": 0.0
    },
    "Rovman Powell": {
        "matches": 31,
        "runs": 1110,
        "wickets": 2,
        "batting_avg": 22.2,
        "bowling_avg": 35.0,
        "strike_rate": 142.31,
        "economy": 11.67
    },
    "Shimron Hetmyer": {
        "matches": 125,
        "runs": 130,
        "wickets": 68,
        "batting_avg": 9.17,
        "bowling_avg": 32.17,
        "strike_rate": 96.75,
        "economy": 7.25
    },
    "Kyle Mayers": {
        "matches": 67,
        "runs": 1966,
        "wickets": 51,
        "batting_avg": 23.52,
        "bowling_avg": 28.82,
        "strike_rate": 145.27,
        "economy": 7.79
    },
    "Romario Shepherd": {
        "matches": 32,
        "runs": 536,
        "wickets": 34,
        "batting_avg": 24.36,
        "bowling_avg": 41.53,
        "strike_rate": 175.16,
        "economy": 11.77
    },
    "Alzarri Joseph": {
        "matches": 28,
        "runs": 83,
        "wickets": 115,
        "batting_avg": 7.3,
        "bowling_avg": 28.03,
        "strike_rate": 87.03,
        "economy": 7.67
    },
    "Odean Smith": {
        "matches": 141,
        "runs": 779,
        "wickets": 1,
        "batting_avg": 43.87,
        "bowling_avg": 0.0,
        "strike_rate": 141.77,
        "economy": 0.0
    },
    "Sherfane Rutherford": {
        "matches": 16,
        "runs": 3602,
        "wickets": 2,
        "batting_avg": 37.15,
        "bowling_avg": 0.0,
        "strike_rate": 151.34,
        "economy": 0.0
    },
    "Obed McCoy": {
        "matches": 54,
        "runs": 428,
        "wickets": 84,
        "batting_avg": 14.9,
        "bowling_avg": 20.28,
        "strike_rate": 99.57,
        "economy": 7.27
    },
    "Rassie van der Dussen": {
        "matches": 51,
        "runs": 2245,
        "wickets": 2,
        "batting_avg": 29.19,
        "bowling_avg": 0.0,
        "strike_rate": 125.83,
        "economy": 0.0
    },
    "David Miller": {
        "matches": 104,
        "runs": 1961,
        "wickets": 4,
        "batting_avg": 23.05,
        "bowling_avg": 0.0,
        "strike_rate": 140.7,
        "economy": 0.0
    },
    "Aiden Markram": {
        "matches": 35,
        "runs": 152,
        "wickets": 95,
        "batting_avg": 12.33,
        "bowling_avg": 20.6,
        "strike_rate": 111.61,
        "economy": 6.88
    },
    "Dewald Brevis": {
        "matches": 25,
        "runs": 1212,
        "wickets": 2,
        "batting_avg": 25.25,
        "bowling_avg": 8.0,
        "strike_rate": 146.02,
        "economy": 16.0
    },
    "Lungi Ngidi": {
        "matches": 28,
        "runs": 8,
        "wickets": 84,
        "batting_avg": 2.0,
        "bowling_avg": 20.69,
        "strike_rate": 44.44,
        "economy": 8.41
    },
    "Tabraiz Shamsi": {
        "matches": 6,
        "runs": 4,
        "wickets": 6,
        "batting_avg": 4.0,
        "bowling_avg": 60.33,
        "strike_rate": 50.0,
        "economy": 9.05
    },
    "Wayne Parnell": {
        "matches": 85,
        "runs": 3280,
        "wickets": 4,
        "batting_avg": 28.0,
        "bowling_avg": 0.0,
        "strike_rate": 158.42,
        "economy": 0.0
    },
    "Keshav Maharaj": {
        "matches": 109,
        "runs": 3464,
        "wickets": 5,
        "batting_avg": 25.66,
        "bowling_avg": 0.0,
        "strike_rate": 124.8,
        "economy": 0.0
    },
    "Duan Jansen": {
        "matches": 2,
        "runs": 0,
        "wickets": 2,
        "batting_avg": 0.0,
        "bowling_avg": 53.0,
        "strike_rate": 0.0,
        "economy": 13.25
    },
    "Donovan Ferreira": {
        "matches": 17,
        "runs": 652,
        "wickets": 2,
        "batting_avg": 27.17,
        "bowling_avg": 41.0,
        "strike_rate": 170.68,
        "economy": 13.67
    },
    "Nandre Burger": {
        "matches": 19,
        "runs": 28,
        "wickets": 42,
        "batting_avg": 14.0,
        "bowling_avg": 27.86,
        "strike_rate": 155.56,
        "economy": 9.67
    },
    "Kane Williamson": {
        "matches": 147,
        "runs": 1397,
        "wickets": 4,
        "batting_avg": 44.49,
        "bowling_avg": 0.0,
        "strike_rate": 155.88,
        "economy": 0.0
    },
    "Devon Conway": {
        "matches": 19,
        "runs": 457,
        "wickets": 147,
        "batting_avg": 9.26,
        "bowling_avg": 24.02,
        "strike_rate": 86.57,
        "economy": 7.71
    },
    "Glenn Phillips": {
        "matches": 47,
        "runs": 3222,
        "wickets": 3,
        "batting_avg": 20.57,
        "bowling_avg": 0.0,
        "strike_rate": 157.15,
        "economy": 0.0
    },
    "Daryl Mitchell": {
        "matches": 120,
        "runs": 3329,
        "wickets": 1,
        "batting_avg": 21.97,
        "bowling_avg": 0.0,
        "strike_rate": 123.45,
        "economy": 0.0
    },
    "Mitchell Santner": {
        "matches": 123,
        "runs": 1376,
        "wickets": 68,
        "batting_avg": 27.16,
        "bowling_avg": 33.13,
        "strike_rate": 148.56,
        "economy": 8.9
    },
    "Tim Southee": {
        "matches": 95,
        "runs": 59,
        "wickets": 146,
        "batting_avg": 13.47,
        "bowling_avg": 22.91,
        "strike_rate": 107.36,
        "economy": 8.8
    },
    "Lockie Ferguson": {
        "matches": 59,
        "runs": 234,
        "wickets": 137,
        "batting_avg": 11.53,
        "bowling_avg": 27.15,
        "strike_rate": 87.94,
        "economy": 9.28
    },
    "Matt Henry": {
        "matches": 87,
        "runs": 571,
        "wickets": 1,
        "batting_avg": 29.98,
        "bowling_avg": 0.0,
        "strike_rate": 151.46,
        "economy": 0.0
    },
    "Ish Sodhi": {
        "matches": 82,
        "runs": 1084,
        "wickets": 2,
        "batting_avg": 43.74,
        "bowling_avg": 0.0,
        "strike_rate": 139.6,
        "economy": 0.0
    },
    "Colin Munro": {
        "matches": 13,
        "runs": 354,
        "wickets": 0,
        "batting_avg": 14.75,
        "bowling_avg": 0.0,
        "strike_rate": 125.53,
        "economy": 7.5
    },
    "Martin Guptill": {
        "matches": 112,
        "runs": 152,
        "wickets": 132,
        "batting_avg": 11.93,
        "bowling_avg": 22.86,
        "strike_rate": 97.2,
        "economy": 8.35
    },
    "Rahmanullah Gurbaz": {
        "matches": 19,
        "runs": 726,
        "wickets": 0,
        "batting_avg": 21.35,
        "bowling_avg": 0.0,
        "strike_rate": 134.94,
        "economy": 0.0
    },
    "Naveen-ul-Haq": {
        "matches": 18,
        "runs": 36,
        "wickets": 50,
        "batting_avg": 18.0,
        "bowling_avg": 23.64,
        "strike_rate": 72.0,
        "economy": 9.16
    },
    "Fazalhaq Farooqi": {
        "matches": 13,
        "runs": 10,
        "wickets": 12,
        "batting_avg": 10.0,
        "bowling_avg": 72.83,
        "strike_rate": 33.33,
        "economy": 10.32
    },
    "Noor Ahmad": {
        "matches": 52,
        "runs": 62,
        "wickets": 122,
        "batting_avg": 2.82,
        "bowling_avg": 24.51,
        "strike_rate": 53.45,
        "economy": 8.17
    },
    "Mujeeb Ur Rahman": {
        "matches": 21,
        "runs": 24,
        "wickets": 40,
        "batting_avg": 4.0,
        "bowling_avg": 31.0,
        "strike_rate": 80.0,
        "economy": 8.34
    },
    "Mohammad Nabi": {
        "matches": 25,
        "runs": 442,
        "wickets": 30,
        "batting_avg": 13.0,
        "bowling_avg": 34.47,
        "strike_rate": 145.39,
        "economy": 7.44
    },
    "Azmatullah Omarzai": {
        "matches": 19,
        "runs": 302,
        "wickets": 30,
        "batting_avg": 15.1,
        "bowling_avg": 37.87,
        "strike_rate": 149.5,
        "economy": 9.63
    },
    "Gulbadin Naib": {
        "matches": 3,
        "runs": 38,
        "wickets": 0,
        "batting_avg": 19.0,
        "bowling_avg": 0.0,
        "strike_rate": 126.67,
        "economy": 12.0
    },
    "Shakib Al Hasan": {
        "matches": 72,
        "runs": 1590,
        "wickets": 126,
        "batting_avg": 19.39,
        "bowling_avg": 29.19,
        "strike_rate": 124.41,
        "economy": 7.44
    },
    "Taskin Ahmed": {
        "matches": 66,
        "runs": 1566,
        "wickets": 25,
        "batting_avg": 15.86,
        "bowling_avg": 26.13,
        "strike_rate": 138.14,
        "economy": 8.02
    },
    "Litton Das": {
        "matches": 35,
        "runs": 1429,
        "wickets": 0,
        "batting_avg": 28.09,
        "bowling_avg": 0.0,
        "strike_rate": 154.98,
        "economy": 0.0
    },
    "Shoriful Islam": {
        "matches": 136,
        "runs": 452,
        "wickets": 4,
        "batting_avg": 37.03,
        "bowling_avg": 0.0,
        "strike_rate": 139.9,
        "economy": 0.0
    },
    "Wanindu Hasaranga": {
        "matches": 48,
        "runs": 33,
        "wickets": 22,
        "batting_avg": 11.16,
        "bowling_avg": 24.57,
        "strike_rate": 124.05,
        "economy": 7.17
    },
    "Maheesh Theekshana": {
        "matches": 39,
        "runs": 34,
        "wickets": 72,
        "batting_avg": 5.67,
        "bowling_avg": 33.53,
        "strike_rate": 50.0,
        "economy": 8.27
    },
    "Dushmantha Chameera": {
        "matches": 84,
        "runs": 1502,
        "wickets": 4,
        "batting_avg": 31.25,
        "bowling_avg": 0.0,
        "strike_rate": 139.21,
        "economy": 0.0
    },
    "Dilshan Madushanka": {
        "matches": 2,
        "runs": 0,
        "wickets": 2,
        "batting_avg": 0.0,
        "bowling_avg": 36.0,
        "strike_rate": 0.0,
        "economy": 9.0
    },
    "Nuwan Thushara": {
        "matches": 9,
        "runs": 0,
        "wickets": 18,
        "batting_avg": 0.0,
        "bowling_avg": 31.44,
        "strike_rate": 0.0,
        "economy": 9.43
    },
    "Bhanuka Rajapaksa": {
        "matches": 97,
        "runs": 558,
        "wickets": 56,
        "batting_avg": 30.8,
        "bowling_avg": 27.84,
        "strike_rate": 145.31,
        "economy": 7.66
    },
    "Dasun Shanaka": {
        "matches": 148,
        "runs": 1735,
        "wickets": 44,
        "batting_avg": 24.07,
        "bowling_avg": 28.27,
        "strike_rate": 151.28,
        "economy": 7.09
    },
    "Kusal Mendis": {
        "matches": 136,
        "runs": 950,
        "wickets": 0,
        "batting_avg": 31.66,
        "bowling_avg": 0.0,
        "strike_rate": 128.4,
        "economy": 0.0
    },
    "Charith Asalanka": {
        "matches": 35,
        "runs": 935,
        "wickets": 89,
        "batting_avg": 29.3,
        "bowling_avg": 21.96,
        "strike_rate": 137.91,
        "economy": 7.25
    },
    "Manish Pandey": {
        "matches": 114,
        "runs": 1588,
        "wickets": 49,
        "batting_avg": 25.76,
        "bowling_avg": 20.31,
        "strike_rate": 152.27,
        "economy": 8.87
    },
    "Deepak Hooda": {
        "matches": 107,
        "runs": 453,
        "wickets": 31,
        "batting_avg": 26.26,
        "bowling_avg": 20.17,
        "strike_rate": 150.84,
        "economy": 8.36
    },
    "Kedar Jadhav": {
        "matches": 123,
        "runs": 2888,
        "wickets": 0,
        "batting_avg": 35.03,
        "bowling_avg": 0.0,
        "strike_rate": 126.25,
        "economy": 0.0
    },
    "Ambati Rayudu": {
        "matches": 113,
        "runs": 223,
        "wickets": 30,
        "batting_avg": 11.53,
        "bowling_avg": 26.23,
        "strike_rate": 83.02,
        "economy": 6.74
    },
    "Robin Uthappa": {
        "matches": 122,
        "runs": 1640,
        "wickets": 2,
        "batting_avg": 25.34,
        "bowling_avg": 0.0,
        "strike_rate": 138.3,
        "economy": 0.0
    },
    "Piyush Chawla": {
        "matches": 73,
        "runs": 133,
        "wickets": 48,
        "batting_avg": 11.36,
        "bowling_avg": 22.7,
        "strike_rate": 105.55,
        "economy": 7.29
    },
    "Amit Mishra": {
        "matches": 163,
        "runs": 762,
        "wickets": 348,
        "batting_avg": 11.91,
        "bowling_avg": 23.82,
        "strike_rate": 90.93,
        "economy": 7.38
    },
    "Ishant Sharma": {
        "matches": 118,
        "runs": 114,
        "wickets": 192,
        "batting_avg": 9.5,
        "bowling_avg": 35.18,
        "strike_rate": 82.61,
        "economy": 8.38
    },
    "Umesh Yadav": {
        "matches": 147,
        "runs": 196,
        "wickets": 87,
        "batting_avg": 13.76,
        "bowling_avg": 27.51,
        "strike_rate": 84.45,
        "economy": 8.52
    },
    "Jaydev Unadkat": {
        "matches": 14,
        "runs": 1408,
        "wickets": 5,
        "batting_avg": 33.06,
        "bowling_avg": 0.0,
        "strike_rate": 154.47,
        "economy": 0.0
    },
    "Siddarth Kaul": {
        "matches": 56,
        "runs": 40,
        "wickets": 116,
        "batting_avg": 5.0,
        "bowling_avg": 29.98,
        "strike_rate": 55.56,
        "economy": 8.63
    },
    "Navdeep Saini": {
        "matches": 6,
        "runs": 4,
        "wickets": 12,
        "batting_avg": 2.0,
        "bowling_avg": 29.0,
        "strike_rate": 100.0,
        "economy": 11.6
    },
    "Shivam Mavi": {
        "matches": 33,
        "runs": 102,
        "wickets": 60,
        "batting_avg": 5.67,
        "bowling_avg": 31.4,
        "strike_rate": 91.07,
        "economy": 8.71
    },
    "Kamlesh Nagarkoti": {
        "matches": 127,
        "runs": 2539,
        "wickets": 4,
        "batting_avg": 31.68,
        "bowling_avg": 0.0,
        "strike_rate": 151.94,
        "economy": 0.0
    },
    "Chetan Sakariya": {
        "matches": 21,
        "runs": 40,
        "wickets": 40,
        "batting_avg": 3.33,
        "bowling_avg": 31.9,
        "strike_rate": 64.52,
        "economy": 8.62
    },
    "Khaleel Ahmed": {
        "matches": 83,
        "runs": 154,
        "wickets": 96,
        "batting_avg": 6.31,
        "bowling_avg": 28.48,
        "strike_rate": 119.87,
        "economy": 9.19
    },
    "T Natarajan": {
        "matches": 74,
        "runs": 8,
        "wickets": 146,
        "batting_avg": 8.0,
        "bowling_avg": 32.58,
        "strike_rate": 57.14,
        "economy": 9.19
    },
    "Shahbaz Ahmed": {
        "matches": 59,
        "runs": 1206,
        "wickets": 54,
        "batting_avg": 20.79,
        "bowling_avg": 39.59,
        "strike_rate": 123.31,
        "economy": 9.79
    },
    "Rahul Tewatia": {
        "matches": 106,
        "runs": 2604,
        "wickets": 64,
        "batting_avg": 23.67,
        "bowling_avg": 34.72,
        "strike_rate": 138.07,
        "economy": 7.91
    },
    "Abdul Samad": {
        "matches": 59,
        "runs": 1718,
        "wickets": 4,
        "batting_avg": 19.09,
        "bowling_avg": 62.5,
        "strike_rate": 148.62,
        "economy": 13.16
    },
    "Mahipal Lomror": {
        "matches": 64,
        "runs": 490,
        "wickets": 118,
        "batting_avg": 8.53,
        "bowling_avg": 24.67,
        "strike_rate": 85.55,
        "economy": 7.8
    },
    "Riyan Parag": {
        "matches": 90,
        "runs": 3758,
        "wickets": 18,
        "batting_avg": 25.39,
        "bowling_avg": 57.22,
        "strike_rate": 144.32,
        "economy": 9.69
    },
    "Shashank Singh": {
        "matches": 46,
        "runs": 1810,
        "wickets": 10,
        "batting_avg": 36.2,
        "bowling_avg": 28.0,
        "strike_rate": 161.61,
        "economy": 9.33
    },
    "Ashutosh Sharma": {
        "matches": 27,
        "runs": 1128,
        "wickets": 0,
        "batting_avg": 29.68,
        "bowling_avg": 0.0,
        "strike_rate": 168.86,
        "economy": 0.0
    },
    "Jitesh Sharma": {
        "matches": 35,
        "runs": 2257,
        "wickets": 0,
        "batting_avg": 30.25,
        "bowling_avg": 0.0,
        "strike_rate": 157.63,
        "economy": 0.0
    },
    "Anuj Rawat": {
        "matches": 22,
        "runs": 636,
        "wickets": 0,
        "batting_avg": 19.88,
        "bowling_avg": 0.0,
        "strike_rate": 119.1,
        "economy": 0.0
    },
    "Srikar Bharat": {
        "matches": 126,
        "runs": 2680,
        "wickets": 0,
        "batting_avg": 38.26,
        "bowling_avg": 0.0,
        "strike_rate": 155.73,
        "economy": 0.0
    },
    "Narayan Jagadeesan": {
        "matches": 11,
        "runs": 324,
        "wickets": 0,
        "batting_avg": 18.0,
        "bowling_avg": 0.0,
        "strike_rate": 110.2,
        "economy": 0.0
    },
    "Sheldon Jackson": {
        "matches": 90,
        "runs": 376,
        "wickets": 106,
        "batting_avg": 6.03,
        "bowling_avg": 28.48,
        "strike_rate": 119.99,
        "economy": 6.52
    },
    "Upendra Yadav": {
        "matches": 74,
        "runs": 1031,
        "wickets": 4,
        "batting_avg": 36.16,
        "bowling_avg": 0.0,
        "strike_rate": 132.75,
        "economy": 0.0
    },
    "Vishnu Vinod": {
        "matches": 8,
        "runs": 142,
        "wickets": 0,
        "batting_avg": 11.83,
        "bowling_avg": 0.0,
        "strike_rate": 109.23,
        "economy": 0.0
    },
    "Harpreet Brar": {
        "matches": 49,
        "runs": 498,
        "wickets": 74,
        "batting_avg": 20.75,
        "bowling_avg": 30.95,
        "strike_rate": 120.87,
        "economy": 8.0
    },
    "Rahul Chahar": {
        "matches": 75,
        "runs": 430,
        "wickets": 148,
        "batting_avg": 13.69,
        "bowling_avg": 23.8,
        "strike_rate": 82.83,
        "economy": 7.49
    },
    "Ravi Bishnoi": {
        "matches": 86,
        "runs": 90,
        "wickets": 166,
        "batting_avg": 3.75,
        "bowling_avg": 30.05,
        "strike_rate": 65.22,
        "economy": 8.36
    },
    "Mayank Markande": {
        "matches": 41,
        "runs": 96,
        "wickets": 74,
        "batting_avg": 16.0,
        "bowling_avg": 30.95,
        "strike_rate": 114.29,
        "economy": 9.16
    },
    "Shreyas Gopal": {
        "matches": 52,
        "runs": 360,
        "wickets": 104,
        "batting_avg": 12.86,
        "bowling_avg": 25.94,
        "strike_rate": 106.51,
        "economy": 8.17
    },
    "Karn Sharma": {
        "matches": 89,
        "runs": 94,
        "wickets": 96,
        "batting_avg": 5.57,
        "bowling_avg": 34.96,
        "strike_rate": 93.33,
        "economy": 8.73
    },
    "Deepak Chahar": {
        "matches": 128,
        "runs": 351,
        "wickets": 19,
        "batting_avg": 6.45,
        "bowling_avg": 29.45,
        "strike_rate": 109.19,
        "economy": 6.74
    },
    "Sameer Rizvi": {
        "matches": 19,
        "runs": 848,
        "wickets": 0,
        "batting_avg": 30.29,
        "bowling_avg": 0.0,
        "strike_rate": 144.71,
        "economy": 0.0
    },
    "Prerak Mankad": {
        "matches": 85,
        "runs": 1644,
        "wickets": 3,
        "batting_avg": 32.83,
        "bowling_avg": 0.0,
        "strike_rate": 139.38,
        "economy": 0.0
    },
    "Vicky Ostwal": {
        "matches": 109,
        "runs": 2439,
        "wickets": 52,
        "batting_avg": 29.75,
        "bowling_avg": 24.28,
        "strike_rate": 140.4,
        "economy": 7.3
    },
    "Abishek Porel": {
        "matches": 34,
        "runs": 1538,
        "wickets": 0,
        "batting_avg": 25.63,
        "bowling_avg": 0.0,
        "strike_rate": 145.37,
        "economy": 0.0
    },
    "Ricky Bhui": {
        "matches": 70,
        "runs": 333,
        "wickets": 5,
        "batting_avg": 39.7,
        "bowling_avg": 0.0,
        "strike_rate": 124.09,
        "economy": 0.0
    },
    "Kumar Kushagra": {
        "matches": 5,
        "runs": 42,
        "wickets": 0,
        "batting_avg": 5.25,
        "bowling_avg": 0.0,
        "strike_rate": 100.0,
        "economy": 0.0
    },
    "Adam Gilchrist": {
        "matches": 80,
        "runs": 2069,
        "wickets": 0,
        "batting_avg": 27.22,
        "bowling_avg": 0.0,
        "strike_rate": 138.39,
        "economy": 0.0
    },
    "Virender Sehwag": {
        "matches": 105,
        "runs": 5456,
        "wickets": 12,
        "batting_avg": 27.56,
        "bowling_avg": 39.17,
        "strike_rate": 155.44,
        "economy": 10.37
    },
    "Zaheer Khan": {
        "matches": 100,
        "runs": 234,
        "wickets": 204,
        "batting_avg": 8.36,
        "bowling_avg": 27.27,
        "strike_rate": 82.98,
        "economy": 7.59
    },
    "Muttiah Muralitharan": {
        "matches": 67,
        "runs": 40,
        "wickets": 128,
        "batting_avg": 3.33,
        "bowling_avg": 26.66,
        "strike_rate": 66.67,
        "economy": 6.7
    },
    "Dale Steyn": {
        "matches": 95,
        "runs": 166,
        "wickets": 97,
        "batting_avg": 8.3,
        "bowling_avg": 25.85,
        "strike_rate": 102.4,
        "economy": 6.91
    },
    "Michael Hussey": {
        "matches": 59,
        "runs": 1977,
        "wickets": 0,
        "batting_avg": 38.76,
        "bowling_avg": 0.0,
        "strike_rate": 122.64,
        "economy": 0.0
    },
    "Jacques Kallis": {
        "matches": 98,
        "runs": 2427,
        "wickets": 65,
        "batting_avg": 28.55,
        "bowling_avg": 35.27,
        "strike_rate": 109.22,
        "economy": 7.89
    },
    "Brendon McCullum": {
        "matches": 109,
        "runs": 2880,
        "wickets": 0,
        "batting_avg": 27.69,
        "bowling_avg": 0.0,
        "strike_rate": 131.74,
        "economy": 0.0
    },
    "Harbhajan Singh": {
        "matches": 164,
        "runs": 1666,
        "wickets": 300,
        "batting_avg": 15.15,
        "bowling_avg": 26.87,
        "strike_rate": 137.91,
        "economy": 7.08
    },
    "Anil Kumble": {
        "matches": 43,
        "runs": 70,
        "wickets": 90,
        "batting_avg": 11.67,
        "bowling_avg": 23.51,
        "strike_rate": 74.47,
        "economy": 6.58
    },
    "Matthew Hayden": {
        "matches": 32,
        "runs": 1107,
        "wickets": 0,
        "batting_avg": 36.9,
        "bowling_avg": 0.0,
        "strike_rate": 137.51,
        "economy": 0.0
    },
    "Shaun Marsh": {
        "matches": 71,
        "runs": 2477,
        "wickets": 0,
        "batting_avg": 39.95,
        "bowling_avg": 0.0,
        "strike_rate": 132.74,
        "economy": 0.0
    },
    "Chris Morris": {
        "matches": 81,
        "runs": 618,
        "wickets": 95,
        "batting_avg": 15.84,
        "bowling_avg": 23.98,
        "strike_rate": 155.27,
        "economy": 8.0
    },
    "Mohsin Khan": {
        "matches": 31,
        "runs": 50,
        "wickets": 76,
        "batting_avg": 5.0,
        "bowling_avg": 24.13,
        "strike_rate": 89.29,
        "economy": 8.41
    },
    "Suyash Prabhudessai": {
        "matches": 43,
        "runs": 903,
        "wickets": 0,
        "batting_avg": 21.77,
        "bowling_avg": 0.0,
        "strike_rate": 143.34,
        "economy": 0.0
    },
    "Akash Deep": {
        "matches": 15,
        "runs": 50,
        "wickets": 20,
        "batting_avg": 8.33,
        "bowling_avg": 54.8,
        "strike_rate": 178.57,
        "economy": 11.83
    },
    "Kumar Kartikeya": {
        "matches": 17,
        "runs": 24,
        "wickets": 24,
        "batting_avg": 3.0,
        "bowling_avg": 33.92,
        "strike_rate": 70.59,
        "economy": 8.66
    },
    "Arjun Tendulkar": {
        "matches": 7,
        "runs": 36,
        "wickets": 8,
        "batting_avg": 18.0,
        "bowling_avg": 37.5,
        "strike_rate": 128.57,
        "economy": 9.28
    },
    "Arshad Khan": {
        "matches": 25,
        "runs": 284,
        "wickets": 36,
        "batting_avg": 23.67,
        "bowling_avg": 37.17,
        "strike_rate": 149.47,
        "economy": 11.03
    },
    "Shahrukh Khan": {
        "matches": 57,
        "runs": 459,
        "wickets": 49,
        "batting_avg": 25.04,
        "bowling_avg": 30.58,
        "strike_rate": 133.35,
        "economy": 8.99
    },
    "R. Sai Kishore": {
        "matches": 38,
        "runs": 41,
        "wickets": 24,
        "batting_avg": 6.56,
        "bowling_avg": 23.77,
        "strike_rate": 91.21,
        "economy": 7.87
    },
    "Yash Dhull": {
        "matches": 16,
        "runs": 1869,
        "wickets": 0,
        "batting_avg": 26.12,
        "bowling_avg": 0.0,
        "strike_rate": 134.89,
        "economy": 0.0
    },
    "Raj Angad Bawa": {
        "matches": 47,
        "runs": 734,
        "wickets": 25,
        "batting_avg": 23.54,
        "bowling_avg": 27.93,
        "strike_rate": 147.32,
        "economy": 7.73
    },
    "Angkrish Raghuvanshi": {
        "matches": 31,
        "runs": 1770,
        "wickets": 0,
        "batting_avg": 34.04,
        "bowling_avg": 0.0,
        "strike_rate": 145.56,
        "economy": 0.0
    },
    "Naman Dhir": {
        "matches": 34,
        "runs": 1420,
        "wickets": 0,
        "batting_avg": 27.31,
        "bowling_avg": 0.0,
        "strike_rate": 163.97,
        "economy": 8.77
    },
    "Shivalik Sharma": {
        "matches": 42,
        "runs": 1301,
        "wickets": 0,
        "batting_avg": 20.46,
        "bowling_avg": 0.0,
        "strike_rate": 137.9,
        "economy": 0.0
    },
    "Nitish Kumar Reddy": {
        "matches": 12,
        "runs": 1169,
        "wickets": 58,
        "batting_avg": 16.32,
        "bowling_avg": 31.19,
        "strike_rate": 127.77,
        "economy": 7.78
    },
    "Vidwath Kaverappa": {
        "matches": 2,
        "runs": 0,
        "wickets": 4,
        "batting_avg": 0.0,
        "bowling_avg": 18.0,
        "strike_rate": 0.0,
        "economy": 9.0
    },
    "Rasikh Salam": {
        "matches": 26,
        "runs": 86,
        "wickets": 58,
        "batting_avg": 8.6,
        "bowling_avg": 28.07,
        "strike_rate": 102.38,
        "economy": 10.01
    },
    "Darshan Nalkande": {
        "matches": 58,
        "runs": 133,
        "wickets": 70,
        "batting_avg": 6.01,
        "bowling_avg": 25.28,
        "strike_rate": 105.67,
        "economy": 7.37
    },
    "Spencer Johnson": {
        "matches": 22,
        "runs": 30,
        "wickets": 72,
        "batting_avg": 10.16,
        "bowling_avg": 21.17,
        "strike_rate": 119.28,
        "economy": 7.35
    },
    "Kwena Maphaka": {
        "matches": 40,
        "runs": 173,
        "wickets": 58,
        "batting_avg": 9.74,
        "bowling_avg": 26.5,
        "strike_rate": 109.08,
        "economy": 7.07
    },
    "Luke Wood": {
        "matches": 3,
        "runs": 18,
        "wickets": 2,
        "batting_avg": 18.0,
        "bowling_avg": 93.0,
        "strike_rate": 300.0,
        "economy": 15.5
    },
    "Shamar Joseph": {
        "matches": 2,
        "runs": 0,
        "wickets": 0,
        "batting_avg": 0.0,
        "bowling_avg": 0.0,
        "strike_rate": 0.0,
        "economy": 11.75
    },
    "Will Jacks": {
        "matches": 44,
        "runs": 874,
        "wickets": 53,
        "batting_avg": 21.44,
        "bowling_avg": 34.42,
        "strike_rate": 126.47,
        "economy": 8.36
    },
    "Aaron Hardie": {
        "matches": 11,
        "runs": 740,
        "wickets": 33,
        "batting_avg": 25.91,
        "bowling_avg": 22.17,
        "strike_rate": 139.64,
        "economy": 7.95
    },
    "Matt Short": {
        "matches": 50,
        "runs": 427,
        "wickets": 21,
        "batting_avg": 26.49,
        "bowling_avg": 32.5,
        "strike_rate": 135.15,
        "economy": 8.33
    },
    "Josh Inglis": {
        "matches": 15,
        "runs": 1016,
        "wickets": 0,
        "batting_avg": 32.77,
        "bowling_avg": 0.0,
        "strike_rate": 131.09,
        "economy": 0.0
    },
    "Riley Meredith": {
        "matches": 16,
        "runs": 50,
        "wickets": 22,
        "batting_avg": 12.93,
        "bowling_avg": 29.3,
        "strike_rate": 109.52,
        "economy": 7.08
    },
    "Lance Morris": {
        "matches": 59,
        "runs": 144,
        "wickets": 26,
        "batting_avg": 11.66,
        "bowling_avg": 25.41,
        "strike_rate": 110.0,
        "economy": 7.86
    },
    "Nathan Ellis": {
        "matches": 10,
        "runs": 238,
        "wickets": 24,
        "batting_avg": 8.68,
        "bowling_avg": 19.6,
        "strike_rate": 110.13,
        "economy": 8.18
    },
    "Jhye Richardson": {
        "matches": 58,
        "runs": 140,
        "wickets": 13,
        "batting_avg": 13.65,
        "bowling_avg": 18.57,
        "strike_rate": 90.09,
        "economy": 9.35
    },
    "Kyle Jamieson": {
        "matches": 16,
        "runs": 61,
        "wickets": 26,
        "batting_avg": 5.05,
        "bowling_avg": 29.81,
        "strike_rate": 108.27,
        "economy": 8.76
    },
    "Ashton Agar": {
        "matches": 34,
        "runs": 483,
        "wickets": 52,
        "batting_avg": 15.89,
        "bowling_avg": 27.46,
        "strike_rate": 154.21,
        "economy": 7.58
    },
    "Michael Bracewell": {
        "matches": 13,
        "runs": 473,
        "wickets": 39,
        "batting_avg": 19.68,
        "bowling_avg": 29.49,
        "strike_rate": 148.89,
        "economy": 8.61
    },
    "Lalit Yadav": {
        "matches": 26,
        "runs": 610,
        "wickets": 20,
        "batting_avg": 19.06,
        "bowling_avg": 42.5,
        "strike_rate": 105.17,
        "economy": 8.85
    },
    "Aman Khan": {
        "matches": 10,
        "runs": 200,
        "wickets": 0,
        "batting_avg": 25.0,
        "bowling_avg": 0.0,
        "strike_rate": 130.0,
        "economy": 0.0
    },
    "Pravin Dubey": {
        "matches": 6,
        "runs": 46,
        "wickets": 4,
        "batting_avg": 23.0,
        "bowling_avg": 55.5,
        "strike_rate": 69.7,
        "economy": 8.54
    },
    "Priyam Garg": {
        "matches": 10,
        "runs": 200,
        "wickets": 0,
        "batting_avg": 25.0,
        "bowling_avg": 0.0,
        "strike_rate": 130.0,
        "economy": 0.0
    },
    "Anmolpreet Singh": {
        "matches": 10,
        "runs": 278,
        "wickets": 0,
        "batting_avg": 15.44,
        "bowling_avg": 0.0,
        "strike_rate": 120.87,
        "economy": 0.0
    },
    "Sanvir Singh": {
        "matches": 6,
        "runs": 50,
        "wickets": 0,
        "batting_avg": 12.5,
        "bowling_avg": 0.0,
        "strike_rate": 119.05,
        "economy": 0.0
    },
    "Harpreet Singh Bhatia": {
        "matches": 10,
        "runs": 200,
        "wickets": 0,
        "batting_avg": 25.0,
        "bowling_avg": 0.0,
        "strike_rate": 130.0,
        "economy": 0.0
    },
    "Swastik Chikara": {
        "matches": 10,
        "runs": 200,
        "wickets": 0,
        "batting_avg": 25.0,
        "bowling_avg": 0.0,
        "strike_rate": 130.0,
        "economy": 0.0
    },
    "Saurav Chauhan": {
        "matches": 4,
        "runs": 36,
        "wickets": 0,
        "batting_avg": 6.0,
        "bowling_avg": 0.0,
        "strike_rate": 120.0,
        "economy": 0.0
    },
    "Avanish Rao Aravelly": {
        "matches": 10,
        "runs": 200,
        "wickets": 0,
        "batting_avg": 25.0,
        "bowling_avg": 0.0,
        "strike_rate": 130.0,
        "economy": 0.0
    },
    "Luvnith Sisodia": {
        "matches": 10,
        "runs": 200,
        "wickets": 0,
        "batting_avg": 25.0,
        "bowling_avg": 0.0,
        "strike_rate": 130.0,
        "economy": 0.0
    },
    "Aryan Juyal": {
        "matches": 10,
        "runs": 200,
        "wickets": 0,
        "batting_avg": 25.0,
        "bowling_avg": 0.0,
        "strike_rate": 130.0,
        "economy": 0.0
    },
    "Bipin Saurabh": {
        "matches": 10,
        "runs": 200,
        "wickets": 0,
        "batting_avg": 25.0,
        "bowling_avg": 0.0,
        "strike_rate": 130.0,
        "economy": 0.0
    },
    "BR Sharath": {
        "matches": 2,
        "runs": 4,
        "wickets": 0,
        "batting_avg": 2.0,
        "bowling_avg": 0.0,
        "strike_rate": 40.0,
        "economy": 0.0
    },
    "Urvil Patel": {
        "matches": 11,
        "runs": 394,
        "wickets": 0,
        "batting_avg": 19.7,
        "bowling_avg": 0.0,
        "strike_rate": 205.21,
        "economy": 0.0
    },
    "Harvik Desai": {
        "matches": 10,
        "runs": 200,
        "wickets": 0,
        "batting_avg": 25.0,
        "bowling_avg": 0.0,
        "strike_rate": 130.0,
        "economy": 0.0
    },
    "G Ajitesh": {
        "matches": 10,
        "runs": 200,
        "wickets": 0,
        "batting_avg": 25.0,
        "bowling_avg": 0.0,
        "strike_rate": 130.0,
        "economy": 0.0
    },
    "Gourav Choudhary": {
        "matches": 10,
        "runs": 200,
        "wickets": 0,
        "batting_avg": 25.0,
        "bowling_avg": 0.0,
        "strike_rate": 130.0,
        "economy": 0.0
    },
    "Aakash Chopra": {
        "matches": 7,
        "runs": 106,
        "wickets": 0,
        "batting_avg": 8.83,
        "bowling_avg": 0.0,
        "strike_rate": 74.65,
        "economy": 0.0
    },
    "Abhinav Mukund": {
        "matches": 3,
        "runs": 38,
        "wickets": 0,
        "batting_avg": 9.5,
        "bowling_avg": 0.0,
        "strike_rate": 86.36,
        "economy": 0.0
    },
    "Abhishek Nayar": {
        "matches": 25,
        "runs": 1946,
        "wickets": 82,
        "batting_avg": 21.85,
        "bowling_avg": 27.93,
        "strike_rate": 143.5,
        "economy": 7.5
    },
    "Aditya Tare": {
        "matches": 84,
        "runs": 3178,
        "wickets": 0,
        "batting_avg": 32.18,
        "bowling_avg": 0.0,
        "strike_rate": 136.78,
        "economy": 0.0
    },
    "Ajit Agarkar": {
        "matches": 101,
        "runs": 274,
        "wickets": 73,
        "batting_avg": 8.5,
        "bowling_avg": 29.72,
        "strike_rate": 109.86,
        "economy": 7.3
    },
    "Akshdeep Nath": {
        "matches": 35,
        "runs": 1817,
        "wickets": 0,
        "batting_avg": 34.72,
        "bowling_avg": 0.0,
        "strike_rate": 147.55,
        "economy": 0.0
    },
    "Ankit Sharma": {
        "matches": 22,
        "runs": 174,
        "wickets": 24,
        "batting_avg": 12.43,
        "bowling_avg": 37.5,
        "strike_rate": 129.85,
        "economy": 7.36
    },
    "Anureet Singh": {
        "matches": 23,
        "runs": 72,
        "wickets": 36,
        "batting_avg": 9.0,
        "bowling_avg": 34.61,
        "strike_rate": 76.6,
        "economy": 9.07
    },
    "Ashish Nehra": {
        "matches": 89,
        "runs": 82,
        "wickets": 212,
        "batting_avg": 5.86,
        "bowling_avg": 23.54,
        "strike_rate": 66.13,
        "economy": 7.85
    },
    "Ashok Dinda": {
        "matches": 24,
        "runs": 293,
        "wickets": 37,
        "batting_avg": 8.44,
        "bowling_avg": 28.54,
        "strike_rate": 113.5,
        "economy": 6.87
    },
    "Baba Aparajith": {
        "matches": 104,
        "runs": 1821,
        "wickets": 53,
        "batting_avg": 23.95,
        "bowling_avg": 21.21,
        "strike_rate": 128.37,
        "economy": 8.43
    },
    "Baba Indrajith": {
        "matches": 4,
        "runs": 42,
        "wickets": 0,
        "batting_avg": 7.0,
        "bowling_avg": 0.0,
        "strike_rate": 70.0,
        "economy": 0.0
    },
    "Baltej Singh": {
        "matches": 115,
        "runs": 31,
        "wickets": 75,
        "batting_avg": 7.93,
        "bowling_avg": 19.08,
        "strike_rate": 99.12,
        "economy": 8.25
    },
    "Barinder Sran": {
        "matches": 52,
        "runs": 112,
        "wickets": 66,
        "batting_avg": 9.34,
        "bowling_avg": 27.76,
        "strike_rate": 116.97,
        "economy": 7.7
    },
    "Basil Thampi": {
        "matches": 26,
        "runs": 64,
        "wickets": 44,
        "batting_avg": 32.0,
        "bowling_avg": 38.45,
        "strike_rate": 91.43,
        "economy": 9.74
    },
    "Bipul Sharma": {
        "matches": 30,
        "runs": 374,
        "wickets": 34,
        "batting_avg": 23.38,
        "bowling_avg": 33.65,
        "strike_rate": 152.03,
        "economy": 8.06
    },
    "Chama Milind": {
        "matches": 108,
        "runs": 82,
        "wickets": 93,
        "batting_avg": 5.13,
        "bowling_avg": 19.69,
        "strike_rate": 93.41,
        "economy": 7.72
    },
    "CM Gautam": {
        "matches": 14,
        "runs": 338,
        "wickets": 0,
        "batting_avg": 16.9,
        "bowling_avg": 0.0,
        "strike_rate": 112.67,
        "economy": 0.0
    },
    "Dhawal Kulkarni": {
        "matches": 112,
        "runs": 94,
        "wickets": 82,
        "batting_avg": 5.39,
        "bowling_avg": 19.38,
        "strike_rate": 93.95,
        "economy": 8.7
    },
    "Gurkeerat Singh Mann": {
        "matches": 25,
        "runs": 1393,
        "wickets": 89,
        "batting_avg": 29.18,
        "bowling_avg": 22.23,
        "strike_rate": 134.98,
        "economy": 8.62
    },
    "Hanuma Vihari": {
        "matches": 63,
        "runs": 2453,
        "wickets": 0,
        "batting_avg": 33.73,
        "bowling_avg": 0.0,
        "strike_rate": 132.84,
        "economy": 0.0
    },
    "Iqbal Abdulla": {
        "matches": 49,
        "runs": 176,
        "wickets": 80,
        "batting_avg": 44.0,
        "bowling_avg": 27.73,
        "strike_rate": 104.76,
        "economy": 7.23
    },
    "Irfan Pathan": {
        "matches": 66,
        "runs": 935,
        "wickets": 32,
        "batting_avg": 24.93,
        "bowling_avg": 23.65,
        "strike_rate": 151.93,
        "economy": 8.45
    },
    "Jalaj Saxena": {
        "matches": 100,
        "runs": 793,
        "wickets": 27,
        "batting_avg": 21.28,
        "bowling_avg": 26.63,
        "strike_rate": 140.76,
        "economy": 8.67
    },
    "Joginder Sharma": {
        "matches": 17,
        "runs": 72,
        "wickets": 24,
        "batting_avg": 9.0,
        "bowling_avg": 34.92,
        "strike_rate": 120.0,
        "economy": 9.82
    },
    "Manan Vohra": {
        "matches": 52,
        "runs": 2166,
        "wickets": 0,
        "batting_avg": 22.1,
        "bowling_avg": 0.0,
        "strike_rate": 130.64,
        "economy": 0.0
    },
    "Mandeep Singh": {
        "matches": 98,
        "runs": 3412,
        "wickets": 0,
        "batting_avg": 20.8,
        "bowling_avg": 0.0,
        "strike_rate": 122.91,
        "economy": 13.0
    },
    "Manpreet Gony": {
        "matches": 101,
        "runs": 127,
        "wickets": 28,
        "batting_avg": 7.08,
        "bowling_avg": 28.65,
        "strike_rate": 104.46,
        "economy": 8.58
    },
    "Mayank Agarwal": {
        "matches": 81,
        "runs": 3312,
        "wickets": 0,
        "batting_avg": 32.81,
        "bowling_avg": 0.0,
        "strike_rate": 121.81,
        "economy": 0.0
    },
    "Manoj Tiwary": {
        "matches": 82,
        "runs": 1053,
        "wickets": 0,
        "batting_avg": 23.23,
        "bowling_avg": 0.0,
        "strike_rate": 128.53,
        "economy": 0.0
    },
    "Milind Kumar": {
        "matches": 39,
        "runs": 2714,
        "wickets": 0,
        "batting_avg": 25.84,
        "bowling_avg": 0.0,
        "strike_rate": 145.81,
        "economy": 0.0
    },
    "Mohammad Kaif": {
        "matches": 23,
        "runs": 518,
        "wickets": 0,
        "batting_avg": 14.39,
        "bowling_avg": 0.0,
        "strike_rate": 103.6,
        "economy": 0.0
    },
    "Munaf Patel": {
        "matches": 20,
        "runs": 112,
        "wickets": 92,
        "batting_avg": 11.8,
        "bowling_avg": 26.93,
        "strike_rate": 86.23,
        "economy": 7.37
    },
    "Murugan Ashwin": {
        "matches": 45,
        "runs": 70,
        "wickets": 70,
        "batting_avg": 3.89,
        "bowling_avg": 33.2,
        "strike_rate": 70.0,
        "economy": 8.01
    },
    "Nathu Singh": {
        "matches": 111,
        "runs": 242,
        "wickets": 78,
        "batting_avg": 10.81,
        "bowling_avg": 26.13,
        "strike_rate": 123.49,
        "economy": 8.14
    },
    "Parthiv Patel": {
        "matches": 119,
        "runs": 1149,
        "wickets": 0,
        "batting_avg": 35.4,
        "bowling_avg": 0.0,
        "strike_rate": 152.24,
        "economy": 0.0
    },
    "Paul Valthaty": {
        "matches": 56,
        "runs": 456,
        "wickets": 71,
        "batting_avg": 21.41,
        "bowling_avg": 29.63,
        "strike_rate": 149.38,
        "economy": 7.59
    },
    "Pawan Negi": {
        "matches": 47,
        "runs": 730,
        "wickets": 68,
        "batting_avg": 14.04,
        "bowling_avg": 27.62,
        "strike_rate": 126.3,
        "economy": 7.87
    },
    "Pragyan Ojha": {
        "matches": 56,
        "runs": 58,
        "wickets": 102,
        "batting_avg": 6.51,
        "bowling_avg": 19.73,
        "strike_rate": 104.07,
        "economy": 8.73
    },
    "Praveen Kumar": {
        "matches": 120,
        "runs": 680,
        "wickets": 180,
        "batting_avg": 8.95,
        "bowling_avg": 36.12,
        "strike_rate": 108.28,
        "economy": 7.73
    },
    "Pravin Tambe": {
        "matches": 21,
        "runs": 291,
        "wickets": 69,
        "batting_avg": 5.51,
        "bowling_avg": 24.89,
        "strike_rate": 108.19,
        "economy": 7.57
    },
    "Rajat Bhatia": {
        "matches": 95,
        "runs": 684,
        "wickets": 142,
        "batting_avg": 11.4,
        "bowling_avg": 28.45,
        "strike_rate": 120.42,
        "economy": 7.41
    },
    "Ramesh Powar": {
        "matches": 54,
        "runs": 42,
        "wickets": 115,
        "batting_avg": 7.85,
        "bowling_avg": 19.31,
        "strike_rate": 122.98,
        "economy": 6.57
    },
    "RP Singh": {
        "matches": 83,
        "runs": 104,
        "wickets": 180,
        "batting_avg": 3.47,
        "bowling_avg": 25.98,
        "strike_rate": 68.42,
        "economy": 7.9
    },
    "Rishi Dhawan": {
        "matches": 38,
        "runs": 420,
        "wickets": 50,
        "batting_avg": 19.09,
        "bowling_avg": 35.64,
        "strike_rate": 112.3,
        "economy": 8.08
    },
    "Sachin Baby": {
        "matches": 14,
        "runs": 288,
        "wickets": 4,
        "batting_avg": 16.0,
        "bowling_avg": 4.0,
        "strike_rate": 122.03,
        "economy": 4.8
    },
    "Sandeep Warrier": {
        "matches": 54,
        "runs": 52,
        "wickets": 72,
        "batting_avg": 7.08,
        "bowling_avg": 26.35,
        "strike_rate": 121.99,
        "economy": 7.73
    },
    "Saurabh Tiwary": {
        "matches": 113,
        "runs": 1228,
        "wickets": 0,
        "batting_avg": 31.32,
        "bowling_avg": 0.0,
        "strike_rate": 131.56,
        "economy": 0.0
    },
    "Shahbaz Nadeem": {
        "matches": 72,
        "runs": 78,
        "wickets": 96,
        "batting_avg": 2.79,
        "bowling_avg": 37.17,
        "strike_rate": 44.83,
        "economy": 7.56
    },
    "Sreesanth": {
        "matches": 71,
        "runs": 281,
        "wickets": 58,
        "batting_avg": 6.85,
        "bowling_avg": 20.7,
        "strike_rate": 123.36,
        "economy": 7.0
    },
    "Stuart Binny": {
        "matches": 50,
        "runs": 893,
        "wickets": 65,
        "batting_avg": 28.81,
        "bowling_avg": 28.81,
        "strike_rate": 128.13,
        "economy": 7.54
    },
    "Swapnil Singh": {
        "matches": 15,
        "runs": 102,
        "wickets": 14,
        "batting_avg": 10.2,
        "bowling_avg": 34.43,
        "strike_rate": 113.33,
        "economy": 8.93
    },
    "Unmukt Chand": {
        "matches": 61,
        "runs": 2168,
        "wickets": 0,
        "batting_avg": 26.49,
        "bowling_avg": 0.0,
        "strike_rate": 122.02,
        "economy": 0.0
    },
    "Varun Aaron": {
        "matches": 85,
        "runs": 181,
        "wickets": 32,
        "batting_avg": 5.62,
        "bowling_avg": 24.02,
        "strike_rate": 123.35,
        "economy": 8.66
    },
    "Vijay Shankar": {
        "matches": 70,
        "runs": 2466,
        "wickets": 18,
        "batting_avg": 26.23,
        "bowling_avg": 38.22,
        "strike_rate": 129.79,
        "economy": 8.67
    },
    "Vinay Kumar": {
        "matches": 63,
        "runs": 270,
        "wickets": 53,
        "batting_avg": 6.1,
        "bowling_avg": 27.19,
        "strike_rate": 98.9,
        "economy": 8.15
    },
    "Wasim Jaffer": {
        "matches": 9,
        "runs": 260,
        "wickets": 0,
        "batting_avg": 16.25,
        "bowling_avg": 0.0,
        "strike_rate": 107.44,
        "economy": 0.0
    },
    "Yusuf Pathan": {
        "matches": 99,
        "runs": 865,
        "wickets": 46,
        "batting_avg": 26.55,
        "bowling_avg": 22.1,
        "strike_rate": 125.79,
        "economy": 7.41
    },
    "Anukul Roy": {
        "matches": 104,
        "runs": 1618,
        "wickets": 68,
        "batting_avg": 29.16,
        "bowling_avg": 22.26,
        "strike_rate": 152.97,
        "economy": 7.53
    },
    "Atharva Taide": {
        "matches": 11,
        "runs": 520,
        "wickets": 0,
        "batting_avg": 26.0,
        "bowling_avg": 0.0,
        "strike_rate": 146.89,
        "economy": 24.0
    },
    "Ajantha Mendis": {
        "matches": 107,
        "runs": 36,
        "wickets": 120,
        "batting_avg": 8.1,
        "bowling_avg": 24.3,
        "strike_rate": 90.13,
        "economy": 7.08
    },
    "Albie Morkel": {
        "matches": 22,
        "runs": 425,
        "wickets": 55,
        "batting_avg": 18.41,
        "bowling_avg": 26.41,
        "strike_rate": 146.4,
        "economy": 7.34
    },
    "Andrew Tye": {
        "matches": 50,
        "runs": 249,
        "wickets": 42,
        "batting_avg": 5.32,
        "bowling_avg": 23.72,
        "strike_rate": 107.65,
        "economy": 8.05
    },
    "Angelo Mathews": {
        "matches": 45,
        "runs": 764,
        "wickets": 68,
        "batting_avg": 27.21,
        "bowling_avg": 28.08,
        "strike_rate": 146.24,
        "economy": 8.46
    },
    "Ben Cutting": {
        "matches": 55,
        "runs": 1994,
        "wickets": 53,
        "batting_avg": 27.34,
        "bowling_avg": 28.09,
        "strike_rate": 131.03,
        "economy": 8.03
    },
    "Brad Hodge": {
        "matches": 69,
        "runs": 2413,
        "wickets": 0,
        "batting_avg": 31.84,
        "bowling_avg": 0.0,
        "strike_rate": 130.62,
        "economy": 0.0
    },
    "Brad Hogg": {
        "matches": 26,
        "runs": 298,
        "wickets": 47,
        "batting_avg": 8.14,
        "bowling_avg": 29.96,
        "strike_rate": 116.18,
        "economy": 8.08
    },
    "Carlos Brathwaite": {
        "matches": 109,
        "runs": 553,
        "wickets": 68,
        "batting_avg": 24.57,
        "bowling_avg": 31.66,
        "strike_rate": 126.31,
        "economy": 8.48
    },
    "Chris Lynn": {
        "matches": 34,
        "runs": 1930,
        "wickets": 0,
        "batting_avg": 26.03,
        "bowling_avg": 0.0,
        "strike_rate": 143.48,
        "economy": 0.0
    },
    "Colin de Grandhomme": {
        "matches": 59,
        "runs": 460,
        "wickets": 61,
        "batting_avg": 18.49,
        "bowling_avg": 22.26,
        "strike_rate": 127.57,
        "economy": 8.75
    },
    "Corey Anderson": {
        "matches": 73,
        "runs": 415,
        "wickets": 50,
        "batting_avg": 21.61,
        "bowling_avg": 30.81,
        "strike_rate": 134.97,
        "economy": 7.44
    },
    "Daniel Christian": {
        "matches": 86,
        "runs": 1429,
        "wickets": 37,
        "batting_avg": 19.53,
        "bowling_avg": 31.05,
        "strike_rate": 147.12,
        "economy": 8.48
    },
    "Daniel Vettori": {
        "matches": 113,
        "runs": 102,
        "wickets": 47,
        "batting_avg": 5.66,
        "bowling_avg": 26.48,
        "strike_rate": 98.93,
        "economy": 6.73
    },
    "Darren Sammy": {
        "matches": 22,
        "runs": 1707,
        "wickets": 49,
        "batting_avg": 25.27,
        "bowling_avg": 29.07,
        "strike_rate": 127.34,
        "economy": 7.62
    },
    "David Hussey": {
        "matches": 114,
        "runs": 583,
        "wickets": 65,
        "batting_avg": 23.7,
        "bowling_avg": 29.31,
        "strike_rate": 147.46,
        "economy": 7.65
    },
    "Dirk Nannes": {
        "matches": 57,
        "runs": 151,
        "wickets": 67,
        "batting_avg": 8.99,
        "bowling_avg": 28.14,
        "strike_rate": 112.05,
        "economy": 7.83
    },
    "Doug Bollinger": {
        "matches": 92,
        "runs": 155,
        "wickets": 62,
        "batting_avg": 11.94,
        "bowling_avg": 22.08,
        "strike_rate": 124.76,
        "economy": 6.68
    },
    "Dwayne Bravo": {
        "matches": 86,
        "runs": 1192,
        "wickets": 49,
        "batting_avg": 27.68,
        "bowling_avg": 22.66,
        "strike_rate": 153.84,
        "economy": 7.94
    },
    "Dwayne Smith": {
        "matches": 95,
        "runs": 1727,
        "wickets": 49,
        "batting_avg": 20.15,
        "bowling_avg": 22.54,
        "strike_rate": 145.02,
        "economy": 7.58
    },
    "Evin Lewis": {
        "matches": 27,
        "runs": 1308,
        "wickets": 0,
        "batting_avg": 27.25,
        "bowling_avg": 0.0,
        "strike_rate": 137.11,
        "economy": 0.0
    },
    "George Bailey": {
        "matches": 74,
        "runs": 3126,
        "wickets": 0,
        "batting_avg": 25.33,
        "bowling_avg": 0.0,
        "strike_rate": 147.07,
        "economy": 0.0
    },
    "Hashim Amla": {
        "matches": 75,
        "runs": 2019,
        "wickets": 0,
        "batting_avg": 33.19,
        "bowling_avg": 0.0,
        "strike_rate": 152.41,
        "economy": 0.0
    },
    "Herschelle Gibbs": {
        "matches": 19,
        "runs": 663,
        "wickets": 0,
        "batting_avg": 31.27,
        "bowling_avg": 0.0,
        "strike_rate": 151.45,
        "economy": 0.0
    },
    "Imran Tahir": {
        "matches": 60,
        "runs": 66,
        "wickets": 164,
        "batting_avg": 8.25,
        "bowling_avg": 20.77,
        "strike_rate": 89.19,
        "economy": 7.76
    },
    "James Faulkner": {
        "matches": 99,
        "runs": 1498,
        "wickets": 26,
        "batting_avg": 27.45,
        "bowling_avg": 30.67,
        "strike_rate": 147.96,
        "economy": 8.45
    },
    "Jason Behrendorff": {
        "matches": 82,
        "runs": 164,
        "wickets": 43,
        "batting_avg": 8.81,
        "bowling_avg": 20.02,
        "strike_rate": 103.71,
        "economy": 8.26
    },
    "Kevon Cooper": {
        "matches": 120,
        "runs": 1513,
        "wickets": 45,
        "batting_avg": 22.14,
        "bowling_avg": 29.4,
        "strike_rate": 129.05,
        "economy": 7.52
    },
    "Lendl Simmons": {
        "matches": 54,
        "runs": 1733,
        "wickets": 0,
        "batting_avg": 32.6,
        "bowling_avg": 0.0,
        "strike_rate": 133.92,
        "economy": 0.0
    },
    "Mahela Jayawardene": {
        "matches": 61,
        "runs": 3281,
        "wickets": 0,
        "batting_avg": 30.48,
        "bowling_avg": 0.0,
        "strike_rate": 120.38,
        "economy": 0.0
    },
    "Marlon Samuels": {
        "matches": 100,
        "runs": 1375,
        "wickets": 54,
        "batting_avg": 27.65,
        "bowling_avg": 30.7,
        "strike_rate": 142.8,
        "economy": 7.33
    },
    "Mitchell Johnson": {
        "matches": 112,
        "runs": 140,
        "wickets": 108,
        "batting_avg": 7.77,
        "bowling_avg": 19.84,
        "strike_rate": 90.88,
        "economy": 7.29
    },
    "Mitchell McClenaghan": {
        "matches": 64,
        "runs": 40,
        "wickets": 97,
        "batting_avg": 5.97,
        "bowling_avg": 24.19,
        "strike_rate": 93.41,
        "economy": 8.79
    },
    "Moises Henriques": {
        "matches": 79,
        "runs": 1765,
        "wickets": 75,
        "batting_avg": 25.19,
        "bowling_avg": 27.13,
        "strike_rate": 136.01,
        "economy": 7.45
    },
    "Morne Morkel": {
        "matches": 71,
        "runs": 252,
        "wickets": 154,
        "batting_avg": 11.45,
        "bowling_avg": 27.13,
        "strike_rate": 140.0,
        "economy": 7.69
    },
    "Nathan Coulter-Nile": {
        "matches": 58,
        "runs": 157,
        "wickets": 99,
        "batting_avg": 8.22,
        "bowling_avg": 28.25,
        "strike_rate": 111.62,
        "economy": 7.13
    },
    "Ross Taylor": {
        "matches": 100,
        "runs": 2998,
        "wickets": 0,
        "batting_avg": 35.59,
        "bowling_avg": 0.0,
        "strike_rate": 131.46,
        "economy": 0.0
    },
    "Ryan ten Doeschate": {
        "matches": 27,
        "runs": 1691,
        "wickets": 75,
        "batting_avg": 20.94,
        "bowling_avg": 31.72,
        "strike_rate": 135.73,
        "economy": 7.72
    },
    "Scott Styris": {
        "matches": 28,
        "runs": 1833,
        "wickets": 88,
        "batting_avg": 25.12,
        "bowling_avg": 30.58,
        "strike_rate": 152.72,
        "economy": 7.75
    },
    "Sean Abbott": {
        "matches": 65,
        "runs": 109,
        "wickets": 103,
        "batting_avg": 6.87,
        "bowling_avg": 19.13,
        "strike_rate": 87.72,
        "economy": 7.55
    },
    "Shaun Tait": {
        "matches": 101,
        "runs": 159,
        "wickets": 48,
        "batting_avg": 8.02,
        "bowling_avg": 24.71,
        "strike_rate": 86.0,
        "economy": 6.82
    },
    "Sheldon Cottrell": {
        "matches": 62,
        "runs": 156,
        "wickets": 51,
        "batting_avg": 8.29,
        "bowling_avg": 28.38,
        "strike_rate": 123.29,
        "economy": 8.92
    },
    "Tymal Mills": {
        "matches": 87,
        "runs": 169,
        "wickets": 83,
        "batting_avg": 11.67,
        "bowling_avg": 25.16,
        "strike_rate": 105.27,
        "economy": 7.64
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
