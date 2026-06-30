import Welcome from "./components/Welcome";
import NavBar from "./components/NavBar";
import CompanyCard from "./components/CompanyCard";
import JobCard from "./components/JobCard";
import Footer from "./components/Footer";
import { useEffect, useState } from "react";
import { getCompanies } from "./Services/CompanyService";
import type { company } from "./types/company";

function App() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);
  const [companies, setCompanies] = useState<company[]>([]);

  async function fetchCompanies() {
    setLoading(true);

    try {
      const data = await getCompanies();
      setCompanies(data);
    } catch (err) {
      setError(err as Error);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    fetchCompanies();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <>
      <Welcome />
      <NavBar />

      <br />

      {companies.map((company) => (
        <CompanyCard
          key={company.id}
          company={company}
        />
      ))}

      <JobCard />
      <Footer />
    </>
  );
}

export default App;