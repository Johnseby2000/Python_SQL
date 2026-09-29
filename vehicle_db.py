import mysql.connector

class VehicleListCreateRetrieveUpdateDelete:

    def __init__(self):
        self.con = mysql.connector.connect(
            user='root',
            password='john',
            host='localhost',
            database='vehicle_db'
        )

        self.cursor = self.con.cursor()

    # LIST ALL VEHICLES
    def list(self):
        query = "SELECT * FROM vehicle"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        if records:
            for vehicle in records:
                print(vehicle)
        else:
            print("No record found")

    # CREATE
    def create(self, id, brand, model, type, price, year):
        query = """
        INSERT INTO vehicle(id, brand, model, type, price, year)
        VALUES(%s, %s, %s, %s, %s, %s)
        """

        data = (id, brand, model, type, price, year)

        self.cursor.execute(query, data)
        self.con.commit()

        print("Inserted data successfully")

    # RETRIEVE
    def retrieve(self, id):
        query = "SELECT * FROM vehicle WHERE id=%s"

        data = (id,)

        self.cursor.execute(query, data)

        record = self.cursor.fetchone()

        if record:
            print(record)
        else:
            print("No record found")

    # UPDATE
    def update(self, id, brand, model, type, price, year):
        query = """
        UPDATE vehicle
        SET brand=%s,
            model=%s,
            type=%s,
            price=%s,
            year=%s
        WHERE id=%s
        """

        data = (brand, model, type, price, year, id)

        self.cursor.execute(query, data)
        self.con.commit()

        if self.cursor.rowcount > 0:
            print("Record updated successfully")
        else:
            print("No record found")

    # DELETE VEHICLE
    def delete(self, id):
        query = "DELETE FROM vehicle WHERE id=%s"

        data = (id,)

        self.cursor.execute(query, data)
        self.con.commit()

        if self.cursor.rowcount > 0:
            print("Record deleted successfully")
        else:
            print("No record found")


# CREATE OBJECT
vehicle_instance = VehicleListCreateRetrieveUpdateDelete()
#
# vehicle_instance.create(
#     101,
#     "Toyota",
#     "Camry",
#     "Sedan",
#     2500000,
#     2024
# )
# vehicle_instance.create(
#     102, "Honda", "City", "Sedan", 1500000, 2023
# )
#
# vehicle_instance.create(
#     103, "Hyundai", "Creta", "SUV", 1800000, 2024
# )
#
# vehicle_instance.create(
#     104, "BMW", "X3", "SUV", 6500000, 2023
# )
#
# vehicle_instance.create(
#     105, "Ford", "Endeavour", "SUV", 3500000, 2022
# )
# LIST
# vehicle_instance.list()

# RETRIEVE
# vehicle_instance.retrieve(102)
#


# # # UPDATE
vehicle_instance.update(
    102,
    "Toyo",
    "Corolla",
    "Sedan",
    200000,
    2025
)
#
#
# # # DELETE
# vehicle_instance.delete(101)