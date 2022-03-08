```mermaid
    graph TD;
        A[Consumer] --> B[Poco];
        B --> E[zlib, openssl, ...];
        A --> C[Producer];
        C -->|build_requires| D[gtest];
```