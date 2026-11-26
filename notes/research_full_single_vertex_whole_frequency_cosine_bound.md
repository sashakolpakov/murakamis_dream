# A whole-frequency bound for the original single-vertex cosine observation

Private finite-source theorem, 9 November 2026. The full
single-vertex angular envelope gives a quadratic exponential
loss for its actual radical cosine observation at every frequency
below one half. An exact finite sampling rectangle, with a
frequency-dependent height, retains both level parities, the
original crossing, all sampling aliases and both vertical currents.
No local packet remainder is separated from the source.

No mathematical numerical evaluation, saved-value calculation or
frozen-source change is used. This is an upper bound, not a
nonzero observation or an adequate volume-budget assertion.

## 1. Source, constants and statement

Fix integers \(n\ne0\) and \(m\). The inner power is \(n\);
the outer crossing power is \(m\). Use
\[
\begin{gathered}
D=N-1,\quad q=e^{\pi i/N},\quad \eta=(-1)^D,\quad
M=\lceil N/2\rceil,\quad U=\lfloor N/2\rfloor-1,\\
c_j=2\cos((2j+1)\pi/N),\qquad
u_j=\pi-(2j+1)\pi/N,\qquad c_j=-2\cos u_j .
\end{gathered}                                                     \tag{1}
\]
Let
\[
Q_{n,N}(u)=P_{n,N}(0,u)
          =\widehat Q_{n,N}(-2\cos u)                               \tag{2}
\]
be the full canonical inner polynomial of
[the single-vertex theorem, equation (1)](research_all_nonzero_degree_two_fillings.md).
Both edges and its internal Hermite trace remain full.
The spectral polynomial \(\widehat Q_{n,N}\) is its original
canonical representative. Define
\[
C_k(X)=T_k(-X/2),\qquad
\mathcal O_{n,m,N,k}
 =\phi_N\!\left[R_N^m e_M\widehat Q_{n,N} C_k\right].
                                                                    \tag{3}
\]
Thus \(C_k(c_j)=\cos(k u_j)\). Using \(T_k(X/2)\) instead
only multiplies the observation by \((-1)^k\).

The cited theorem supplies \(c_n,B_n,b_n,C_n'>0\) and a
finite exponent \(a_n\) such that
\[
|Q_{n,N}(x+iy)|
\le C_n'N^{a_n}
 \exp N\{M_n-c_n(1-\cos x)+B_n y^2\},
\quad |x|\le\pi,\quad |y|\le b_n,                                  \tag{4}
\]
where \(M_n=\Re S_n(0,0)\) has the original action
normalization. The bound holds through both level parities.
For \(n=\pm1,\pm2\), retain precisely the phase and scalar
conventions in that theorem. This argument uses (4), not a
replacement geometric normalization for those powers.

Put
\[
\begin{split}
K_{n,m}&=B_n+\frac{m^2}{16c_n}>0,\\
\tau_{n,m}&=\min\left\{b_n,\frac1{2K_{n,m}}\right\}>0,\\
\gamma_{n,m}
 &=\min\left\{\frac{\tau_{n,m}}2,\frac{c_n}{4}\right\}>0 .
\end{split}                                                       \tag{5}
\]

**Theorem.** At all sufficiently large levels of both parities,
uniformly over integers \(0\le k\le\lfloor N/2\rfloor\),
\[
\boxed{\quad
|\mathcal O_{n,m,N,k}|
\le C_{n,m}N^{a_n+1}
 \exp N\left\{M_n-\gamma_{n,m}
                         \left(\frac12-\frac{k}{N}\right)^2\right\}.
\quad}                                                            \tag{6}
\]
The powers are fixed before \(N\) tends to infinity; constants
are not uniform over unbounded \(n,m\). At even levels the
endpoint \(k=N/2\) is exactly zero.

## 2. The exact parity fold

Write
\[
a_N(u)=
\begin{cases}
\sin u,&N\ \mathrm{even},\\[1mm]
\displaystyle\frac{\sin u\sin(u/2)}
                       {\cos^2(\pi/(2N))},&N\ \mathrm{odd},
\end{cases}
\qquad
\chi_N=
\begin{cases}
i,&N\ \mathrm{even},\\
-1,&N\ \mathrm{odd}.
\end{cases}                                                       \tag{7}
\]
Then \(a_N(-u)=\eta a_N(u)\), and \(a_N\) is uniformly
bounded on each fixed complex horizontal strip for \(N\ge3\).
The original consumed-normal formula is
\[
\mathcal O_{n,m,N,k}
 =\sum_{j=0}^{U}(-1)^{U+j}a_N(u_j)
       R_N(c_j)^m Q_{n,N}(u_j)\cos(k u_j).                          \tag{8}
\]
This is the full radical contraction in
[the Casimir observation, equations (15)--(16)](research_mixed_next_three_outer_casimir_observation.md).
It consumes the outer double-node normals exactly; the inner
normals in \(Q_{n,N}\) remain. The odd simple node \(-2\)
is killed by \(e_M(-2)=0\).

For every signed integer \(m\), the exact crossing value is
\[
R_N(c_j)^m
 =C_{N,m}\exp\!\left(\frac{imN u_j^2}{4\pi}\right),
\qquad
C_{N,m}=\exp\!\left(\frac{\pi i mD^2}{4N}\right).
                                                                    \tag{9}
\]
This is [the original Gaussian crossing identity](research_current_free_aw_crossing_transport.md),
used after the radical reduced the outer trace to values.
No off-grid identification of crossing normals is required.

For
\[
                         \delta=\frac12-\frac{k}{N}\in[0,1/2],
                                                                    \tag{10}
\]
the physical grid satisfies
\[
(-1)^j=e^{i\pi D/2}e^{-iNu_j/2},\qquad
e^{-iNu_j}=\eta,\qquad
e^{-iNu_j/2}\cos(k u_j)
 =\frac12\left(e^{-iN\delta u_j}
                         +\eta e^{iN\delta u_j}\right).            \tag{11}
\]
The source \(Q_{n,N}\) and the Gaussian are even.
Reflection \(j\mapsto D-j\) pairs positive and negative grid
angles. At odd levels the added center has \(a_N(0)=0\).
Since \((-1)^Ue^{i\pi D/2}=\chi_N\), (8)--(11) give
\[
\boxed{\quad
\mathcal O_{n,m,N,k}
 =\frac{\chi_N C_{N,m}}2
   \sum_{j=0}^{D}a_N(u_j)Q_{n,N}(u_j)
       \exp N\left(\frac{im u_j^2}{4\pi}-i\delta u_j\right).
\quad}                                                            \tag{12}
\]
The factor \(1/2\), scalar and all \(N\) grid points are fixed
before taking bounds. At even levels \(k=N/2\) gives
\(\cos(Nu_j/2)=0\) on every double node. The bound (6)
at \(\delta=0\) also follows directly from (4),(8).

## 3. The strip estimate with the crossing retained

Abbreviate \(c=c_n\), \(B=B_n\), \(b=b_n\),
\(K=K_{n,m}\), and \(\tau=\tau_{n,m}\). Put
\[
f_{N,\delta}(u)
 =a_N(u)Q_{n,N}(u)
             \exp N\left(\frac{im u^2}{4\pi}-i\delta u\right).
                                                                    \tag{13}
\]
This is an exact entire function. For \(|x|\le\pi\),
\[
1-\cos x=2\sin^2(x/2)\ge\frac{2x^2}{\pi^2},
\]
and completing the square gives
\[
-\frac{2c x^2}{\pi^2}
       +\frac{|m|\,|x|\,|y|}{2\pi}
\le-\frac{c x^2}{\pi^2}+\frac{m^2y^2}{16c}.                       \tag{14}
\]
The exact real parts of the crossing and character in (13),
together with (4),(14), imply
\[
|f_{N,\delta}(x+iy)|
\le C N^{a_n}
 \exp N\left\{M_n-\frac{c x^2}{\pi^2}+K y^2+\delta y\right\},
\qquad |x|\le\pi,\quad |y|\le b/2.                                \tag{15}
\]
The possible crossing growth has thus been absorbed using the
actual angular loss. The constant includes the bounded parity
amplitude on the fixed strip.

## 4. Exact sampling, all aliases and both verticals

The physical grid is the portion in \((-\pi,\pi)\) of
\[
\frac{2\pi}{N}(\mathbb Z+\rho_N),\qquad
\rho_N=
\begin{cases}1/2,&N\ \mathrm{even},\\0,&N\ \mathrm{odd}.
\end{cases}
\]
Take symmetric midpoint cuts
\[
T_N=\frac{2\pi}{N}
 \left(\left\lfloor\frac N4-\rho_N\right\rfloor
                                     +\rho_N+\frac12\right).
                                                                    \tag{16}
\]
Then \(|T_N-\pi/2|\le\pi/N\); for large \(N\),
\(\pi/4\le T_N\le3\pi/4\), and at both cuts
\[
                       \eta e^{-iN(\pm T_N)}=-1.                   \tag{17}
\]
For \(\delta>0\), choose
\[
                             h=\tau\delta .
                                                                    \tag{18}
\]
Thus \(0<h\le b/2\). The integer-frequency condition implies
\[
                    \delta\ge\frac1{2N},\qquad Nh\ge\frac\tau2 .
                                                                    \tag{19}
\]
Small positive distances from one half therefore do not produce
an unbounded sampling denominator.

The exact simple-pole kernel
\[
                        H_N(u)=\frac1{1-\eta e^{-iNu}}             \tag{20}
\]
has residue \(1/(iN)\) at every physical grid point. On the
positively oriented rectangle
\(\mathcal R_{N,\delta}=[-T_N,T_N]+i[-h,h]\), residues give
\[
\sum_{|u_j|<T_N}f_{N,\delta}(u_j)
       =\frac N{2\pi}\oint_{\partial\mathcal R_{N,\delta}}
                            H_N(u)f_{N,\delta}(u)\,du.             \tag{21}
\]
This is a finite identity. It assumes no periodicity of
\(f_{N,\delta}\) or its Gaussian crossing.

On the lower and upper horizontal sides respectively,
\[
|H_N(x-ih)|\le\frac1{1-e^{-Nh}},\qquad
|H_N(x+ih)|\le\frac{e^{-Nh}}{1-e^{-Nh}}.                            \tag{22}
\]
Equation (19) bounds the denominators uniformly in \(N,k\).
The lower side has rate at most \(M_n+Kh^2-\delta h\);
the upper side has rate at most
\(M_n+Kh^2-(1-\delta)h\). Since \(\delta\le1/2\) and
\(K\tau\le1/2\), both are at most
\[
                         M_n-\frac\tau2\delta^2 .                  \tag{23}
\]
The full rational factors in (22) retain every sampling alias,
including the equality of the two leading costs at \(\delta=1/2\).

On either midpoint vertical the exact modulus is
\[
                  |H_N(\pm T_N+iy)|=\frac1{1+e^{Ny}}.              \tag{24}
\]
For \(y\le0\) use \(|H_N|\le1\); for \(y\ge0\) use
\(|H_N|\le e^{-Ny}\). Combining with (15) and
\(1-\delta\ge\delta\) bounds the rate on either full side by
\[
M_n-\frac{cT_N^2}{\pi^2}+Ky^2-\delta|y|
                     \le M_n-\frac c{16}.                         \tag{25}
\]
Indeed \(|y|\le\tau\delta\) and \(K\tau\le1/2\).
The bound includes \(y=0\), so no zero-height connector is omitted.

All contour lengths are bounded. Hence (21)--(25) give
\[
\left|\sum_{|u_j|<T_N}f_{N,\delta}(u_j)\right|
\le C N^{a_n+1}
       \left(e^{N(M_n-\tau\delta^2/2)}
                              +e^{N(M_n-c/16)}\right).             \tag{26}
\]

## 5. Removed nodes and conclusion

On real nodes the character and crossing in (13) have modulus
one and \(a_N\) is bounded. For \(|u_j|\ge T_N\ge\pi/4\),
(4) and the same angular inequality imply
\[
|Q_{n,N}(u_j)|\le C N^{a_n}e^{N(M_n-c/8)}.
\]
There are at most \(N\) removed nodes, and therefore
\[
\sum_{|u_j|\ge T_N}|f_{N,\delta}(u_j)|
                    \le C N^{a_n+1}e^{N(M_n-c/8)} .                \tag{27}
\]
This includes every original far node, including those tending
to \(\pm\pi\), at both parities.

Finally \(\delta^2\le1/4\), and the choice (5) gives
\[
\gamma_{n,m}\delta^2\le\frac\tau2\delta^2,\qquad
\gamma_{n,m}\delta^2\le\frac c{16}<\frac c8 .
                                                                    \tag{28}
\]
Apply (26)--(28) to the exact fold (12), whose outside
scalar has modulus \(1/2\). This proves (6) for \(\delta>0\).
The already handled endpoint proves the whole statement.

## 6. Scope of the improvement

Every fixed \(0<\alpha<1/2\) now gives a uniform fixed loss
\(\gamma_{n,m}(1/2-\alpha)^2\) for all modes \(k/N\le\alpha\).
Near one half there is a quadratic loss with an explicit
positive coefficient in the existing source constants.
The full polynomial was retained throughout.

The earlier [radical observation theorem](research_radical_observation_boundary_decay.md)
uses an exact finite contour to obtain strict loss at the
unmodulated observation, uniformly over radical indices.
The present statement fixes the midpoint radical and tracks
all cosine frequencies, including their level-dependent
distance to one half. It does not replace a stronger local
selected-action asymptotic near that endpoint.

The constants (5) have not been compared with the complete
actual \(343\) transfer budget. For example, an outgoing
polynomial with the
[adopted angular coefficient rate profile](research_mixed_next_outgoing_action_weighted_green_ellipse.md)
\(\mathcal E(1/2+k/N,Z)\) is bounded after observation by a
polynomial times the maximum of the combined rates
\[
M_3+\mathcal E(1/2+t,Z)-\gamma_{3,3}(1/2-t)^2,
                              \qquad 0\le t\le1/2.                 \tag{29}
\]
Any positive rate tolerances in the input profile must also
be retained. An adequate strict comparison of (29) with the
original transfer action remains a separate requirement.
Positivity of \(\gamma_{3,3}\) alone supplies no such comparison.
Nor is a general finite-exception theorem for arbitrary short
fillings inferred.

## 7. Frozen source bindings

| Source | SHA-256 |
|---|---|
| Full single-vertex theorem | 7ac634d458e5805e95a7ce064d4e1fc513c96c0b758cfaee9f91fd46de10304c |
| Exact Casimir observation | cbbc62951666d06e0ae77b29f49f563d91c2024dc8da900ae996144d7db39dab |
| Original crossing transport | f81b9fc3edc2504c5250ad283bf0ceff191a1fc3a310c00fdb57602362f0bf4a |
| Earlier radical observation bound | 96eedbe601afeebbbf15e4961b1300215bcbbbef2a8c20c3e09977340db9eff9 |
| Actual outgoing coefficient profile | e39abb76185b6969901b6ee4c95a4f947bdda5f74d8ff57062ed4b6591a0c029 |
