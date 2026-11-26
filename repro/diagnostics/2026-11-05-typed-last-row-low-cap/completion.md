# Completed low-height typed last-row subset

The exact subset proposed in
[the design note](../../../notes/research_mixed_typed_last_row_support_design.md)
is now completely certified and independently replayed. For own type three,
the first external input ranges over the full slanted chord \(S_3\) of
\(K_3\); the second ranges over the entire bottom cap of \(K_4\),
\(-.108\le\Im a\le-.102\). For every point of this product, both
original conditional orientations, every revived carrier
\((v,w)\in\{0,1\}^2\), and every target
\(X\in[11/50,9/20]^2\), the exact allocated deficit (3) in that note satisfies
\[
 D_{vw}(Z,X)<-\frac1{1000000}.
\]
This includes the original chirp, both literal allocation flags, the
quadratic supporting-plane correction, and the complete target maximum.
It retains the same original coupled root and response throughout.

The subset is the closed chart
\[
\begin{split}
c_-&=49/125-9i/125,\qquad
c_+=233/625+3\sqrt{16906}/10000
       +i(-49/625+\sqrt{16906}/10000),\\
c(t)&=(1-t)c_-+tc_+,\qquad
h(u)=-27/250+(3/500)u,\\
a(u,v)&=3/10+(2v-1)
 \sqrt{(3/50)^2-(h(u)+13/250)^2}+ih(u),
\qquad(t,u,v)\in[0,1]^3 .
\end{split}
\]
Its boundary equalities and radicand lower bound \(29/62500>0\)
are exact. No floating membership test or independently chosen output
leg enters the conclusion.

## Completion and independent replay

The [original pilot README](README.md), driver, design, and incomplete
record remain unchanged and are pinned by the
[separate continuation driver](continue_subset.py). The continuation
imported all 253 accepted cells verbatim and worked only on descendants
of the six saved pending boxes. It used 292 additional visits and accepted
149 new cells, below its 4095-node/30-second limits.

The resulting [256-bit record](continuation.json) has 402 accepted cells,
803 total tree nodes, no pending frontier, and exact parameter coverage
equal to one. It completed in 1.224 seconds.

The root agent then ran the sole [320-bit saved replay](continuation-replay.json).
It revalidated all 402 original-log affine witnesses and all
\(402\cdot24=9648\) carrier/target envelope bounds, using the saved
rational target trials. It made zero root or target proposals and zero
refinements. Its exact tree, witnesses, and target inventory agree with
the author record; all 33 dependency bindings are current.

The largest saved replay upper bound is approximately
\(-4.5625095810\cdot10^{-6}\).
The conservative displayed gap \(1/1000000\) was extracted by comparing
the exact decimal upper endpoints of all 9648 saved intervals with
\(-1/1000000\). This extraction recomputed no source values, roots, or cells.

## Remaining scope

The remaining part of this same boundary case has the second input above
\(-.102\) in \(K_4\). The other 27 generator cases of the original
28-case design are also outside this completed record.

Moreover, the whole slanted chord has \(\Im c<-.065\) and
\(\Re c>.391\), so it lies outside both actual type-three role domains
\(O_3\) and \(A_3\). This proves a strict comparison on one sufficient
typed-envelope subset. It is not an actual-open-word realization,
a complete typed-domain last-row theorem, or a new finite-source
noncancellation result.

## Provenance

| Artifact | SHA256 |
|---|---|
| Frozen design | 1fe596a46cc050a871f2b8f70427e42e47672de6ede78c79b714056248a3b840 |
| Frozen original pilot | 7a4bf27dca2f87cf600573ea697f2e55924b8eb2b811664cdff4d81881c29b48 |
| Frozen original record | 3032ec6861743b8bd2e73e9d477e90173db847365442640b25c2be8225ce26e4 |
| Continuation/replay driver | 4da575ffe6016d30c7c82671b2acc5dc417179e05beb0d1c9955dc6644206ca5 |
| Complete author record | 00b83fd73691bc24f1bf6e41db8481263eea39978912311c0b724a7b72b2cf69 |
| Independent replay | 9c532b9c0aea845f2e7ac4913d848e0f45078f3e500e567f734ac267c004697a |

Both runs were performed once by the root agent. This completion note
does not alter the pinned original README or replace its historical
incomplete-pilot statement.
