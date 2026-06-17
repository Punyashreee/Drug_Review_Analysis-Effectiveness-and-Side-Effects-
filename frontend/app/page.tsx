"use client";

import { useState } from "react";
import axios from "axios";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
 Tooltip,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
} from "recharts";

export default function Home() {

  const [drugName, setDrugName] = useState("");

  const [review, setReview] = useState("");

  const [loading, setLoading] = useState(false);

  const [result, setResult] = useState<any>(null);

  // -------------------------------------------------
  // API CALL
  // -------------------------------------------------

  const analyzeDrug = async () => {

    if (!drugName.trim()) {

      alert("Please enter drug name");

      return;
    }

    try {

      setLoading(true);

      setResult(null);

      const response = await axios.post(
        "http://127.0.0.1:8000/predict",
        {
          drug_name: drugName,
          review: review,
        }
      );

      console.log(response.data);

      setResult(response.data);

    } catch (error) {

      console.error(error);

      alert("Backend Error");

    } finally {

      setLoading(false);
    }
  };

  // -------------------------------------------------
  // CHART DATA
  // -------------------------------------------------

  const effectivenessData = [
    {
      name: "Effectiveness",
      score: result?.effectiveness_score || 0,
    },
  ];

  const riskData = [
    {
      name: "Risk",
      value: result?.risk_score || 0,
    },
    {
      name: "Safe",
      value: 100 - (result?.risk_score || 0),
    },
  ];

  const COLORS = ["#ff4d4f", "#22c55e"];

  // -------------------------------------------------
  // UI
  // -------------------------------------------------

  return (

    <div className="min-h-screen bg-[#07111f] text-white p-8">

      {/* HEADER */}

      <div className="text-center mb-10">

        <h1 className="text-5xl font-bold text-cyan-400">
          DrugRev AI
        </h1>

        <p className="text-gray-400 mt-4 text-lg">
          AI Drug Review Analysis using NLP + RAG + Transformers
        </p>

      </div>

      {/* INPUT SECTION */}

      <div className="bg-[#101c2c] p-8 rounded-3xl shadow-2xl max-w-4xl mx-auto">

        {/* Drug Name */}

        <div className="mb-5">

          <label className="block mb-2 text-cyan-300 font-semibold">
            Drug Name
          </label>

          <input
            type="text"
            placeholder="Example: Ibuprofen"
            value={drugName}
            onChange={(e) => setDrugName(e.target.value)}
            className="w-full p-4 rounded-xl bg-[#1a2b40] border border-cyan-700 focus:outline-none"
          />

        </div>

        {/* Review */}

        <div className="mb-5">

          <label className="block mb-2 text-cyan-300 font-semibold">
            Review (Optional)
          </label>

          <textarea
            placeholder="Enter your own review..."
            value={review}
            onChange={(e) => setReview(e.target.value)}
            className="w-full p-4 rounded-xl bg-[#1a2b40] border border-cyan-700 h-40 focus:outline-none"
          />

        </div>

        {/* Button */}

        <button
          onClick={analyzeDrug}
          disabled={loading}
          className="w-full bg-cyan-500 hover:bg-cyan-600 transition-all p-4 rounded-xl text-xl font-bold"
        >

          {loading ? "Analyzing..." : "Analyze Drug"}

        </button>

      </div>

      {/* ERROR */}

      {result?.error && (

        <div className="bg-red-500/20 border border-red-500 p-6 rounded-2xl max-w-3xl mx-auto mt-10">

          <h2 className="text-red-400 text-xl font-bold">
            {result.error}
          </h2>

        </div>
      )}

      {/* RESULTS */}

      {result && !result.error && (

        <div className="max-w-7xl mx-auto mt-10">

          {/* TOP CARDS */}

          <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-6 gap-5">

            {/* Drug */}

            <div className="bg-[#101c2c] p-6 rounded-2xl">

              <h2 className="text-gray-400 mb-2">
                Drug
              </h2>

              <p className="text-2xl font-bold text-cyan-300">
                {result.drug_name}
              </p>

            </div>

            {/* Sentiment */}

            <div className="bg-[#101c2c] p-6 rounded-2xl">

              <h2 className="text-gray-400 mb-2">
                Sentiment
              </h2>

              <p
                className={`text-2xl font-bold ${
                  result.sentiment === "POSITIVE"
                    ? "text-green-400"
                    : "text-red-400"
                }`}
              >
                {result.sentiment}
              </p>

            </div>

            {/* Effectiveness */}

            <div className="bg-[#101c2c] p-6 rounded-2xl">

              <h2 className="text-gray-400 mb-2">
                Effectiveness
              </h2>

              <p className="text-2xl font-bold text-blue-400">
                {result.effectiveness}
              </p>

            </div>

            {/* Safety */}

            <div className="bg-[#101c2c] p-6 rounded-2xl">

              <h2 className="text-gray-400 mb-2">
                Safety
              </h2>

              <p
                className={`text-2xl font-bold ${
                  result.safe_to_use === "Safe"
                    ? "text-green-400"
                    : "text-pink-400"
                }`}
              >
                {result.safe_to_use}
              </p>

            </div>

            {/* Average Rating */}

            <div className="bg-[#101c2c] p-6 rounded-2xl">

              <h2 className="text-gray-400 mb-2">
                Avg Rating
              </h2>

              <p className="text-2xl font-bold text-yellow-400">
                {result.average_rating}
              </p>

            </div>

            {/* Review Count */}

            <div className="bg-[#101c2c] p-6 rounded-2xl">

              <h2 className="text-gray-400 mb-2">
                Reviews
              </h2>

              <p className="text-2xl font-bold text-orange-400">
                {result.review_count}
              </p>

            </div>

          </div>

          {/* CHARTS */}

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-8">

            {/* Effectiveness Chart */}

            <div className="bg-[#101c2c] p-6 rounded-2xl">

              <h2 className="text-xl font-bold mb-4 text-cyan-300">
                Effectiveness Score
              </h2>

              <ResponsiveContainer width="100%" height={300}>

                <BarChart data={effectivenessData}>

                  <XAxis dataKey="name" />

                  <YAxis domain={[0, 100]} />

                  <Tooltip />

                  <Bar
                    dataKey="score"
                    fill="#22d3ee"
                  />

                </BarChart>

              </ResponsiveContainer>

            </div>

            {/* Risk Chart */}

            <div className="bg-[#101c2c] p-6 rounded-2xl">

              <h2 className="text-xl font-bold mb-4 text-cyan-300">
                Risk Analysis
              </h2>

              <ResponsiveContainer width="100%" height={300}>

                <PieChart>

                  <Pie
                    data={riskData}
                    cx="50%"
                    cy="50%"
                    outerRadius={100}
                    dataKey="value"
                    label
                  >

                    {riskData.map((entry, index) => (

                      <Cell
                        key={index}
                        fill={COLORS[index % COLORS.length]}
                      />

                    ))}

                  </Pie>

                  <Tooltip />

                </PieChart>

              </ResponsiveContainer>

            </div>

          </div>

          {/* SIDE EFFECTS */}

          <div className="bg-[#101c2c] p-6 rounded-2xl mt-8">

            <h2 className="text-2xl font-bold mb-4 text-cyan-300">
              Side Effects
            </h2>

            {result.side_effects?.length > 0 ? (

              <div className="flex flex-wrap gap-3">

                {result.side_effects.map(
                  (effect: string, index: number) => (

                    <div
                      key={index}
                      className="bg-red-500/20 border border-red-500 px-4 py-2 rounded-full"
                    >

                      {effect}

                    </div>
                  )
                )}

              </div>

            ) : (

              <p className="text-green-400">
                No major side effects detected
              </p>

            )}

          </div>

          {/* ALTERNATIVES */}

          <div className="bg-[#101c2c] p-6 rounded-2xl mt-8">

            <h2 className="text-2xl font-bold mb-4 text-cyan-300">
              Alternative Drugs
            </h2>

            {result.alternatives?.length > 0 ? (

              <div className="flex flex-wrap gap-3">

                {result.alternatives.map(
                  (drug: string, index: number) => (

                    <div
                      key={index}
                      className="bg-cyan-500/20 border border-cyan-500 px-4 py-2 rounded-full"
                    >

                      {drug}

                    </div>
                  )
                )}

              </div>

            ) : (

              <p className="text-gray-400">
                No alternatives found
              </p>

            )}

          </div>

          {/* TOP REVIEWS */}

          <div className="bg-[#101c2c] p-6 rounded-2xl mt-8">

            <h2 className="text-2xl font-bold mb-4 text-cyan-300">
              Top Reviews
            </h2>

            <div className="space-y-4">

              {result.top_reviews?.map(
                (review: string, index: number) => (

                  <div
                    key={index}
                    className="bg-[#16273d] p-4 rounded-xl border border-cyan-800"
                  >

                    {review}

                  </div>
                )
              )}

            </div>

          </div>

          {/* SIMILAR REVIEWS */}

          {result.similar_reviews?.length > 0 && (

            <div className="bg-[#101c2c] p-6 rounded-2xl mt-8 mb-10">

              <h2 className="text-2xl font-bold mb-4 text-cyan-300">
                Similar Reviews (RAG)
              </h2>

              <div className="space-y-4">

                {result.similar_reviews.map(
                  (review: string, index: number) => (

                    <div
                      key={index}
                      className="bg-[#16273d] p-4 rounded-xl border border-cyan-800"
                    >

                      {review}

                    </div>
                  )
                )}

              </div>

            </div>
          )}

        </div>
      )}

    </div>
  );
}