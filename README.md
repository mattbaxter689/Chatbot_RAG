## Initial Commit

This is a simple RAG chatbot that I have plans at some point in the future to
upgrade. For now, we use PgVector as our vector store, langchain for the utility
in setting up the db, and hugging face for models. We also use Gradio to deploy
the app.

### Notes:
At this moment, I am looking at the best way to structure this project. In my
brain, it's best to have a class that handles a pydantic model to create the
string for the DB connection, then another class that handles the PGVector
database itself, that can be used in other classes by calling it (This may
change. Could increase response time to the application) but my thought is that
this will allow for more fine tuning of the specific needs at certain locations.
As well as a separate class that handles loading and splitting of the data. I
will look to implement similar items in the interface and llm directories as
well. For now, the next steps are:
- [ ] Create class that handles the llm creation and tokenization
- [ ] Create user prompt to accept and query data from db
- [ ] Convert user query to relevant output based on the documents
- [ ] Create Gradio App
- [ ] Get data hosted externally on minio

#### Future additions
At some point in the future, I would like to add the following:
- [ ] reranking rag output
- [ ] Possibly using an agent (But perhaps not)
- [ ] implementing a semantic search
- [ ] Hosting as an API

etc
