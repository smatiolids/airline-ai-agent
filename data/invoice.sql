use default_keyspace;
    INSERT INTO invoices (
        customer_id, flight_id, invoice_id, installment_due_dates, installment_plan,
        issue_date, payment_method, status, total_amount
    ) VALUES (
        f08a6894-1863-491d-8116-3945fb915597, c7c01f18-ab35-4b99-bed0-2b54042d647d, 089d88e3-15a7-41af-8c1e-fd3d41eab0ee, 
        {1: '2024-11-01T10:30:00', 2: '2024-11-15T10:30:00', 3: '2024-11-29T10:30:00'}, {1: 116.67, 2: 116.67, 3: 116.67}, '2024-11-01T10:30:00',
        'Credit Card', 'Unpaid', 350.0
    );
    

    INSERT INTO invoices (
        customer_id, flight_id, invoice_id, installment_due_dates, installment_plan,
        issue_date, payment_method, status, total_amount
    ) VALUES (
        f08a6894-1863-491d-8116-3945fb915597, ae4ef50a-1b8e-428f-a892-73010a9f509f, d14b9c30-3e3f-4586-9b87-3325d0690ff0, 
        {1: '2024-10-20T14:00:00', 2: '2024-11-03T14:00:00', 3: '2024-11-17T14:00:00'}, {1: 400.0, 2: 400.0, 3: 400.0}, '2024-10-20T14:00:00',
        'Credit Card', 'Unpaid', 1200.0
    );
    

    INSERT INTO invoices (
        customer_id, flight_id, invoice_id, installment_due_dates, installment_plan,
        issue_date, payment_method, status, total_amount
    ) VALUES (
        f08a6894-1863-491d-8116-3945fb915597, 65c71a9a-734b-4a22-9f4e-ff8e95aaf944, 83609561-569b-42d6-949c-571139b305bf, 
        {1: '2024-11-05T09:45:00', 2: '2024-11-19T09:45:00', 3: '2024-12-03T09:45:00'}, {1: 66.67, 2: 66.67, 3: 66.67}, '2024-11-05T09:45:00',
        'Credit Card', 'Unpaid', 200.0
    );
    

    INSERT INTO invoices (
        customer_id, flight_id, invoice_id, installment_due_dates, installment_plan,
        issue_date, payment_method, status, total_amount
    ) VALUES (
        f08a6894-1863-491d-8116-3945fb915597, b1871210-7342-472f-ba49-394412ccd8ee, be944866-3e4e-4a49-bd7f-91c0a5b33eb5, 
        {1: '2024-11-10T11:15:00', 2: '2024-11-24T11:15:00', 3: '2024-12-08T11:15:00'}, {1: 216.67, 2: 216.67, 3: 216.67}, '2024-11-10T11:15:00',
        'Credit Card', 'Unpaid', 650.0
    );
    

    INSERT INTO invoices (
        customer_id, flight_id, invoice_id, installment_due_dates, installment_plan,
        issue_date, payment_method, status, total_amount
    ) VALUES (
        f08a6894-1863-491d-8116-3945fb915597, 3ccddaf5-a83e-4919-a70a-0434a8f7315c, 745839c7-9ce3-4f31-b8b7-ba289f3812e0, 
        {1: '2024-11-15T08:00:00', 2: '2024-11-29T08:00:00', 3: '2024-12-13T08:00:00'}, {1: 166.67, 2: 166.67, 3: 166.67}, '2024-11-15T08:00:00',
        'Credit Card', 'Unpaid', 500.0
    );
    