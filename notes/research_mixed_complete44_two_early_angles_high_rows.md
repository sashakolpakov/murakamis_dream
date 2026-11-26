# Complete own-four high rows for arbitrary angles in the real half period

Private written proof, 11 November 2026. The original own-four
conditional sum has a half/last-row upper bound when both real
arguments belong to \((0,1/2)\) and both heights are nonpositive.
The first height may have the full actual first-four depth.
The proof retains the radial smoothing coupled to that depth;
it does not discard the reflected drift.

This pays the entire positive upper block by two exact continuous
rates. It does not yet calibrate those rates after attaching the
complete first cap and next kernel, or prove a bound for the
full \(44\) prefix on the early second interval.

## 1. Literal rows and the precise domain

Put
\[
 a=x+ic,\quad y=q+id,\qquad 0<x,q<1/2,
 \qquad -39/500\le c\le0,\quad d\le0 .
 \tag{1}
\]
All uniform finite statements below are on a fixed compact set
of these parameters. In particular they apply to an actual word
beginning \(444\), with \(c=c_1\in(-.078,-.020)\) and
\(d=c_2\in(-.102,-.001)\), as stated in equation (2) of the
[negative first-left source](research_mixed_complete44_second_selected_negative_left_connection.md).
The broader angular domain and range of \(c\) in (1) are proved
independently of actual-word realization. They include intermediate
nonpositive first heights. This is only a row estimate; no change
of actual reference is made in its application.

With \(r_N=e^{-2\pi i/N}\), retain
\[
 P_j=(r_N;r_N)_j,\quad p_j(V)=(r_NV;r_N)_j,\quad
 X=e^{-2\pi ia},\quad Y=e^{-2\pi iy},
\]
\[
 R_{j,N}(a,y)=X^{-j}\frac{p_j(X)p_j(Y)}{P_j^3},
 \qquad C_{1,N}(X,Y)=\sum_{j=0}^{N-1}R_{j,N}(a,y).
 \tag{2}
\]
The full denominator, incoming chirp and stopping index are
unchanged. Define the original absolute row rate
\[
\begin{split}
 E_1(t;a,y)
 &=I_a(t)+I_y(t)-3J(t)-2\pi ct,\qquad 0\le t\le1,\\
 I_b(t)&=\int_0^t\log|1-e^{-2\pi i(b+s)}|\,ds,\qquad
 J(t)=\int_0^t\log(2\sin\pi s)\,ds .
\end{split}
 \tag{3}
\]
Every real zero is integrated. Let
\[
 \lambda=-2\pi c.
 \tag{4}
\]
The original height bound gives
\[
 0\le\lambda\le39\pi/250<1/2.
 \tag{5}
\]
**Theorem 1.** On (1),
\[
 \boxed{\quad
 \max_{1/2\le t\le1}E_1(t;a,y)
       =\max\{E_1(1/2;a,y),\,E_1(1;a,y)\},
 \qquad E_1(1;a,y)=\lambda .
 \quad}
 \tag{7}
\]
Consequently, for every \(\tau>0\), at both level parities,
\[
 \boxed{\quad
 \sum_{j=\lceil N/2\rceil}^{N-1}|R_{j,N}(a,y)|
 \le C_\tau N^{B_\tau}
       \exp N\{\max(E_1(1/2;a,y),\lambda)+\tau\}.
 \quad}
 \tag{8}
\]
The endpoint \(t=1\) in (7) is a continuous rate controlling
the actual index \(N-1\). No new finite row \(j=N\) is inserted.

## 2. Original reflection and two estimates with different roles

Use the original radial primitive
\[
 G_H(t)=\Re g(t-iH),\qquad
 f_H(t)=G_H'(t)=\log|1-e^{-2\pi H-2\pi it}|,\qquad H\ge0 .
 \tag{9}
\]
The [reflection source](research_mixed_right_tail_reflection.md)
proves that \(G_H\) is odd and one-periodic,
\[
 J(t)\le G_H(t)\le0\quad(0\le t\le1/2),
 \tag{10}
\]
and \(f_H\) is even and increasing in distance from the nearest
integer on the real half period. The same source's exact
reciprocal-radius identity gives, for \(v=1-t\),
\[
\begin{split}
 \Phi(v)&=E_1(1-v)-E_1(1)\\
 &=G_{-c}(x-v)-G_{-c}(x)
   +G_{-d}(q-v)-G_{-d}(q)+3J(v)-\lambda v .
\end{split}
 \tag{11}
\]
The mean of each numerator logarithm is zero at nonpositive
height, so \(E_1(1)=\lambda\). The drift in (11) is exactly
coupled to the first radial height; it is not an independent
parameter introduced into the source.

Both reflected arcs \([x-v,x]\) and \([q-v,q]\) lie in
\([-1/2,1/2]\) for every \(0\le v\le1/2\). An even integrand
increasing with absolute argument has its smallest integral on
the centered interval of a given length. Consequently
\[
 \Phi(v)\le
 3J(v)-2G_{-c}(v/2)-2G_{-d}(v/2)-\lambda v .
 \tag{12}
\]
At zero radial height this is interpreted by the integrable
logarithmic limit. In particular the formula remains valid at
all zero-height parameter faces.

The all-angle leg inequality, Lemma 1 of
[the high-row sign-class source](research_mixed_all_angle_high_row_sign_class.md),
is valid for every \(H\ge0\); the lemma itself does not use
that note's sign condition on the original heights:
\[
 G_H(b-v)+J(v)+G_H(1/2-b)\le0,\qquad
 0<b<1/2,\quad0\le v\le1/2 .
 \tag{13}
\]
Subtracting the half-row case of (11) and applying (13) to
both legs yields the useful bound
\[
\begin{split}
 \Phi(v)-\Phi(1/2)
 ={}&[G_{-c}(x-v)+J(v)+G_{-c}(1/2-x)]\\
    &+[G_{-d}(q-v)+J(v)+G_{-d}(1/2-q)]
                       +J(v)+\lambda(1/2-v)\\
 \le{}&J(v)+\lambda(1/2-v),
                    \qquad 0<x,q<1/2,\quad0\le v\le1/2 .
\end{split}
 \tag{14}
\]
Equation (14) alone is insufficient for all heights on the
small \(v\) interval. The next section retains the missing
radial saving instead.

## 3. Small reflected indices and the coupled radial saving

Put
\[
 B(v)=3J(v)-4J(v/2).
 \tag{15}
\]
For \(0<t\le9/100\), the sine lower bound and
\(\log(1-u)\ge-u/(1-u)\) give
\[
 \log(2\sin\pi t)\ge\log(2\pi t)-\frac{\pi^2t^2}{5}.
 \tag{16}
\]
Indeed \((\pi t)^2<1\), so
\((\pi t)^2/(6-(\pi t)^2)\le(\pi t)^2/5\).
Together with \(\sin\pi t\le\pi t\), integration proves
\[
 B(v)\le
 v\{\log(8\pi v)-1\}+\frac{\pi^2v^3}{30},
                    \qquad 0<v\le9/50 .
 \tag{17}
\]

For \(0<v\le1/10\), this gives
\[
 B(v)<-\frac7{150}v.
 \tag{18}
\]
To check the constants, \(\log(4\pi/5)<19/20\), since
\[
 e^{19/20}>
 1+\frac{19}{20}+\frac{361}{800}+\frac{6859}{48000}
 =\frac{122119}{48000}>\frac{88}{35}>\frac{4\pi}{5}.
 \tag{19}
\]
Thus (17), \(\pi^2<10\), and \(v^2\le1/100\) give
\(B(v)<v(-1/20+1/300)=-7v/150\).
Equations (10) and (12) now imply
\[
                \Phi(v)\le B(v)-\lambda v<0
                  \qquad(0<v\le1/10).
 \tag{20}
\]
These rows are bounded by the last rate, for every height
in (1), without any lower angular restriction.

First suppose \(0\le\lambda\le7/20\). The elementary sine
upper bound gives
\[
 J(1/10)\le\frac1{10}\{\log(\pi/5)-1\}<-\frac7{50}.
 \tag{21}
\]
Indeed \(\pi/5<2/3\) and
\(\log(3/2)>2/5\). Since \(J''(v)=\pi\cot(\pi v)\ge0\)
on \((0,1/2]\) and \(J(1/2)=0\), its chord on
\([1/10,1/2]\) gives
\[
 J(v)<-\frac7{20}(1/2-v)\qquad(1/10\le v<1/2).
 \tag{22}
\]
Equations (14), (21), and (22) bound this whole interval by
the half-row.

Now suppose \(7/20\le\lambda<1/2\), and restrict temporarily
to \(1/10\le v\le9/50\). In (12) retain the first radial
saving and use (10) only on the second leg.

On the original lower-disk branch,
\[
 \partial_HG_H(t)
 =\frac\pi2-\pi t
       -\arctan\{\tanh(\pi H)\cot(\pi t)\},\qquad 0<t<1/2.
 \tag{23}
\]
This is equation (10) of
[the deep-negative-height source](research_mixed_early_three_deep_negative_first_height.md).
It follows directly by factoring
\(1-e^{-2\pi H-2\pi it}\); the real arctangent is principal.
Its continuous value at \(H=0\) has the same lift.
Using \(\arctan u\le u\), \(\tanh u\le u\), and
\(\cot t\le1/t\), integration gives, for every \(H\ge0\),
\[
 2\{G_H(v/2)-J(v/2)\}
 \ge\pi H(1-v)-\frac{2H^2}{v}.
 \tag{24}
\]
Here \(H=-c=\lambda/(2\pi)\). Put
\[
 S(\lambda,v)=\frac{\lambda(1+v)}2
                         -\frac{\lambda^2}{2\pi^2v}.
 \tag{25}
\]
Equations (12) and (24) prove
\[
                             \Phi(v)\le B(v)-S(\lambda,v).
 \tag{26}
\]

The right side of (17) increases on \([1/10,9/50]\).
At \(v=9/50\), it is bounded by
\[
 B(v)<\frac{12}{125}+\frac{243}{125000}
       =\frac{12243}{125000}<\frac1{10}.
 \tag{27}
\]
Here \(\pi^2<10\) and \(\log(36\pi/25)<23/15\).
For the latter, the positive exponential series gives
\[
 e^{3/2}>
 1+\frac32+\frac98+\frac9{16}+\frac{27}{128}
   =\frac{563}{128},\qquad e^{1/30}>\frac{31}{30},
 \qquad
 e^{23/15}>\frac{17453}{3840}>
                    \frac{792}{175}>\frac{36\pi}{25}.
 \tag{28}
\]

The saving \(S\) increases with \(v\). It also increases
with \(\lambda\) on the rectangle now used. Indeed
\(\pi^2>48/5\), and
\[
 \partial_\lambda S
 =\frac{1+v}{2}-\frac{\lambda}{\pi^2v}
 >\frac{1+v}{2}-\frac5{96v}
 \ge\frac{11}{20}-\frac{25}{48}>0 .
 \tag{29}
\]
Thus
\[
 S(\lambda,v)>
       \frac{77}{400}-\frac{49}{768}>\frac18.
 \tag{30}
\]
The final comparison is \(19600<20736\). Equations
(26), (27), and (30) prove
\[
                     \Phi(v)<-\frac1{40},
 \qquad 1/10\le v\le9/50,\quad7/20\le\lambda<1/2.
 \tag{31}
\]
These rows are bounded by the literal last rate. In particular
the drift and smoothing were never estimated independently.

## 4. The remaining reflected interval for every angle

Here is a sufficient bound at the left endpoint, proved from
the same primitive rather than an evaluated action:
\[
                         -J(1/6)>\frac{29}{180}.
 \tag{32}
\]
For \(0\le t\le\pi/6\), use
\(\sin t\le t(1-t^2/6+t^4/120)\) and \(\log(1+u)\le u\).
Integration, \(\log(\pi/3)<1/21\), \(\pi>25/8\), and
\(\pi^2<10\) give
\[
 -J(1/6)>
 \frac{10}{63}+\frac{625}{248832}-\frac1{46656}
                         >\frac{29}{180}.
 \tag{33}
\]
The last comparison reduces to \(1859\cdot420>746496\).

On \([1/6,9/50]\),
\(2\sin\pi t\le9\pi/25<198/175<6/5\), so
\(J'(t)<\log(6/5)<1/5\). Hence
\[
 -J(9/50)>\frac{29}{180}-\frac1{375}
           =\frac{713}{4500}.
 \tag{34}
\]
This pays the largest actual drift:
\[
 \frac{713}{4500}>\frac{3432}{21875}
       >\frac{39\pi}{250}\frac8{25}.
 \tag{35}
\]
The first cross-product difference is \(152875>0\);
the second inequality uses \(\pi<22/7\).
Since \(J(1/2)=0\), convexity and (34)--(35) give
\[
 J(v)+\lambda(1/2-v)<0
          \qquad 9/50\le v<1/2.
 \tag{36}
\]
Use (14) to conclude
\[
 \Phi(v)<\Phi(1/2)\qquad(9/50\le v<1/2).
 \tag{37}
\]

Equations (20), (22), (31), and (37), together with
\(\Phi(0)=0\), cover every \(0\le v\le1/2\).
They prove (7) for the entire angular domain (1).

## 5. Every finite physical index and the remaining calibration

The complete uniform row estimate follows from Section 2 of
the [original contour-allowance proof](research_mixed_conditional_contour_allowance.md),
in its zero-safe form in Corollary 3 of the all-angle source.
This portion of the proof requires no critical-point or
retained-contour hypothesis. Replace a numerator logarithm by
\(\log(|1-e^{-2\pi i(a+t)}|+\delta)\), and likewise for \(y\).
For fixed \(\delta>0\), the Riemann-sum errors are uniform on
each compact parameter set in (1). The integral error tends
uniformly to zero as \(\delta\) tends to zero; all possible
real zeros are simple and have the original integrable local
bound \(O(\delta(1+|\log\delta|))\). The denominator factorial
retains its uniform \(O(\log N)\) error through every \(j<N\).
The exact incoming chirp supplies \(-2\pi cj/N\).

Consequently, for any prescribed \(\tau>0\), each physical
row has modulus at most a polynomial times
\(\exp N\{E_1(j/N)+\tau/2\}\). Apply (7) and sum fewer
than \(N\) rows to obtain (8). Both parities and every row
through \(N-1\) are included. A half-grid convention shifting
the first high index by \(O(1)\) is covered by the same
continuity and tolerance. No numerator zero is divided out.

The rate \(E_1(1/2)\) is not a possibly vanishing finite
half-row value. Every subset of the high block inherits (8).
The original factors \(U_{1,N}(w,X)\), \(d_N(X)\), any
first Fourier monomial, the complete next \(C_{1,N}(Y,Z)\),
and its exact allocations may be multiplied on both sides
without alteration. The theorem does not itself bound these
outside factors or remove their possible zeros.

For the remaining early second-period problem, (8) reduces
the first upper physical block to its exact half and last
rates even when both outside real angles are early. More generally,
it removes the angular restrictions from that row reduction
throughout the real half period. Calibration of those two rates
with the complete cap and the next kernel, and the other
first-coordinate path pieces, remain separate. No estimate
for \(R_{44,N}\) or the complete second period is inferred here.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_right_tail_reflection.md | e3928f2d9549159f6955c654b202dc87198137f4cfdb80f85151af567a976ce1 |
| research_mixed_all_angle_high_row_sign_class.md | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| research_mixed_early_three_deep_negative_first_height.md | 60c2ffc14a6776e29b3e1f86e1d1aa52602422f112c5d2ab91675302c2797058 |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |
| research_mixed_complete44_second_selected_negative_left_connection.md | 878cbd67c6035f6fb9903e76d0b719cae599874d852710d979282e711d7fbf77 |

Author full proof readback and all five directly used source
implications and hash checks are complete. Independent full proof
and direct-source review is required before adoption. No mathematical
numerical evaluation, saved-value arithmetic, test, import, compilation
or frozen-source edit is used.
