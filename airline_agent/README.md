# Airline AI Agent with Langflow and DataStax Astra DB

Follow the instructions in YouTube:

- Database setup
- Creating Langflow

## Database Setup

You should have a DataStax Astra account and then create a database.

To create an account, you can use this link: https://bit.ly/ds-langflow

After creating an account, you can create a database. 

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

You can follow the instruction in the video. But here is the JSON file you can import into Langflow to create the flow:

[Airline Agent.json](Airline%20Agent.json)

# Langsmith

You can use the Langsmith to track the flow. Here is the link to the Langsmith dashboard: https://smith.langchain.com/

To enable the Langsmith, you can set the environment variable `LANGCHAIN_TRACING_V2=true` and `LANGCHAIN_API_KEY=lsv2_...`.

# Contact

If you have any questions, please contact me at:

- Email: [samuel.matioli@datastax.com](mailto:samuel.matioli@datastax.com)
- LinkedIn: [@samuelmatioli](https://www.linkedin.com/in/samuelmatioli/)
- Website: [langflow.com](https://langflow.com)
- DataStax: [datastax.com](https://bit.ly/ds-langflow)
