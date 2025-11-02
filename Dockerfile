# 1️⃣ Use a lightweight Python image
FROM python:3.10-slim

# 2️⃣ Set working directory
WORKDIR /app

# 3️⃣ Copy dependency list
COPY requirements.txt .

# 4️⃣ Install Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy all project files into the container
COPY . .

# 6️⃣ Expose the port Flask uses
EXPOSE 5000

# 7️⃣ Command to start your Flask app
CMD ["python", "app.py"]