CREATE TABLE readings (
	reading_id 					integer PRIMARY KEY,
	reading_time						integer,
	lake_id						integer,
	port_number 				integer,
	svc 						text,

	FOREIGN KEY(scan_id)		REFERENCES scans(scan_id),
	FOREIGN KEY(host_id)		REFERENCES hosts(host_id),
	FOREIGN KEY(plugin_id) 		REFERENCES vulns(plugin_id)
);

CREATE TABLE waterbody