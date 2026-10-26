# Ui Demo Deployed at https://resqtravel.netlify.app/

Travel Disruption Recovery Agent

An assistant that watches a whole trip, spots when a delay will break it, and offers the traveller affordable ways to recover. Built for Problem Statement 4.1, Shyadri 26 / Dev Host hackathon.

The Problem

When a flight or train runs late, everything booked after it is at risk: connections are missed, hotels release rooms after check-in closes, and stranded travellers pay surge fares while seats on other services sit empty. Most travel apps treat each booking (each PNR) separately, so a delay is never linked to the rest of the trip, and alerts say what happened but not what to do next.

How It Works
Ticket reading. The traveller uploads an e-ticket, an IRCTC SMS or a hotel PDF. Gemini 2.5 Flash, running in JSON schema mode, turns it into structured trip data. Bookings are saved as nodes and the transfers between them as edges, each with a minimum buffer time.
Conflict detection. A fixed rule, not the model, checks every edge. The delay is applied (A′ = A + Δt), the margin is calculated (M = next departure − A′), and if M < B_min the edge is marked BROKEN_DEPENDENCY.
Search and ranking. Adapters query flight inventory, IRCTC Current Booking and OSRM road routing. Results are filtered by budget, deadline and travel mode, then Gemini scores them and presents three plans:
Alpha: fastest
Beta: cost-neutral
Gamma: nearby hub plus a cab
Notify and recover. The traveller picks a plan in one tap. The system produces a delay proof from the PNR record, sends the hotel a late check-in note, and delivers messages by WhatsApp or email.
