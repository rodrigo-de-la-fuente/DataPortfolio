total_movies = 1500
total_revenue = 5000000.0 #$
total_runtime = 120.5 #minutes

average_runtime = total_runtime / total_movies
average_revenue = total_revenue / total_movies

if average_revenue > 10_000:
    print(f"The average revenue per movie is ${average_revenue:.1f}: greater than $10,000.")
else:
    print(f"The average revenue per movie is ${average_revenue:.1f}: less than $10,000.")
