# Airline AI Agent with Langflow and DataStax Astra

Follow the instructions in YouTube:

- Database setup
- Creating Langflow


## Database Setup

We will load DataStax Astra to store the data. 

You should have a DataStax Astra account and then create a database. 

### Loading the flight tickets data

Access the database and create a collection `flight_tickets`. After that, you can load the flight tickets data into the collection using the file `data/tickets.json`. 

NOTE: If you want to generate a new file, use this prompt along with your favorite LLM:

```
generate a sample json file with flight tickets considering the following attributes:

_id 
passengerId
passengerName
flightNumber
departureAirport
arrivalAirport
departureDateTime
arrivalDateTime
seatNumber
ticketClass
ticketPrice
bookingDate
bookingReference

```

### Loading the invoice data

On the Astra DB Dashboard, access the CQL Console to create a regular Cassandra table. Run the following CQL commands:

```
CREATE TABLE default_keyspace.invoices (
    customer_id uuid,
    flight_id uuid,
    invoice_id uuid,
    installment_due_dates map<int, timestamp>,
    installment_plan map<int, decimal>,
    issue_date timestamp,
    payment_method text,
    status text,
    total_amount decimal,
    PRIMARY KEY (customer_id, flight_id, invoice_id)
) WITH CLUSTERING ORDER BY (flight_id ASC, invoice_id ASC);

```

After that, you can load the invoice data into the table running the commands from the file `data/invoice.sql` on the CQL Console. 

## Creating the Langflow Agent Flow

