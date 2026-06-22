  1. Temporarily lower the signed URL expiration to 1 minute

  In api/src/infrastructure/services/s3-storage/s3-storage.service.ts:202, change:

  // From
  expirationMinutes: number = 60
  // To
  expirationMinutes: number = 1

  2. Revert to the old behaviour (store URL instead of path)

  In api/src/application/services/trust-exchange/trust-exchange-config.service.ts, temporarily change the upload to
  store the URL:

  // From
  logoUrl: uploadResult.path
  // To
  logoUrl: uploadResult.url

  3. Upload a logo
  - Go to the Trust Exchange config page as an admin
  - Upload any image as the logo
  - Confirm the logo appears in the preview

  4. Wait 1 minute

  5. Refresh the public trust exchange page
  - The logo is gone (broken image / 403 from S3)

  3. Revert both temporary changes when done testing.



# Db Cleanup 

 DB cleanup (if ever needed): If any old records still have full URLs stored in logo_url, run:

  -- Find affected records
  SELECT id, logo_url FROM trust_exchange WHERE logo_url LIKE 'https://%';

  -- Option A: Clear them (falls back to org logo)
  UPDATE trust_exchange SET logo_url = NULL WHERE logo_url LIKE 'https://%';

  -- Option B: Extract the S3 key
  UPDATE trust_exchange
  SET logo_url = split_part(regexp_replace(logo_url, '^https://[^/]+/', ''), '?', 1)
  WHERE logo_url LIKE 'https://%';