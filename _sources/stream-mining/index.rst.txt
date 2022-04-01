Stream Mining
=============

Stream mining is the practice of data mining a continuous stream of data records. This data stream either arrives too fast or the complete stream is too large such that it is not feasible to process using conventional data mining techniques, even ones that are tailored for big data.

One common aspect of data mining streams is that it has to be processed quickly, usually as soon as the data arrives. We do not have the luxury of first storing and then analyzing the data at a later time that is more convenient. In this chapter we will show the techniques for doing the following analysis on streaming data:

.. toctree::
   :maxdepth: 1

   stream-data-model
   data-stream
   filtering-stream
   counting-distinct
   moments
   counting-ones
   common-recent

Most of the algorithms for stream mining involve summarizing the stream in some way. These techniques utilizes hash functions in their implementation. In most cases, it will be better to just get the "approximate" answer bounded by some error, instead of getting the exact answer which may not be feasible to compute.
