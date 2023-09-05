import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Eduvocate - Create your future career</title>
        <meta name="description" content="A mentoring platform" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          Welcome to Eduvocate
        </h1>

        <p className={styles.description}>
          Powered by Future Ready foundation.
        </p>

        <div className={styles.grid}>
         Get Ready for a excellent career guidance...
        </div>
      </main>

      <footer className={styles.footer}>
        <div>copy right Eduvocate @ 2023</div>
      </footer>
    </div>
  )
}
