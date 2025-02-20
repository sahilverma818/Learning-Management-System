import React from "react";
import Hero from "../../Components/Hero/Hero";
import Trusted from "../../Components/Trusted/Trusted";
import Detail from "../../Components/Detail/Detail";
import Info from "../../Components/Info/Info";
import InDemandCourses from "../../Components/InDemandCourses/InDemandCourses";

const Home = () => {
    return (
        <div>
            <Hero/>
            <Trusted/>
            <Detail/>
            <InDemandCourses/>
            <Info />
        </div>
    )
}

export default Home