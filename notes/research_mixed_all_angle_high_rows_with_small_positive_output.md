# Complete own-four high rows with the selected positive output height

Private written deduction, 11 November 2026. Retaining both radial
savings extends the all-angle half/last principle to the full
reflected drift needed by an actual first-four height and a selected
outgoing height \(1/100\). The statement bounds the entire positive
physical high block. Calibration of its two remaining rates after
attachment to a cap and a next factor remains separate.

## 1. Literal source and height budget

Let
\[
 a=x+ic,\quad b=q+id,\qquad 0\le x,q\le1/2,\qquad
 (-c)_++d_+\le11/125.                                           \tag{1}
\]
Uniform finite assertions are on a fixed compact set of heights.
In particular (1) includes
\[
 -.078\le c\le1/100,\qquad d=1/100,                              \tag{2}
\]
and every intermediate first height in the complete \(44\)
coefficient paths. It also includes nonpositive outgoing heights
with the previously allowed first depth.

For \(r_N=e^{-2\pi i/N}\), retain
\[
 P_j=(r_N;r_N)_j,\quad p_j(V)=(r_NV;r_N)_j,\quad
 X=e^{-2\pi ia},\quad Y=e^{-2\pi ib},\qquad
 R_{j,N}=X^{-j}\frac{p_j(X)p_j(Y)}{P_j^3}.                        \tag{3}
\]
All rows through \(N-1\), the incoming chirp and the own-four
denominator are unchanged. Define the original full row rate
\[
\begin{split}
 E(t)&=I_a(t)+I_b(t)-3J(t)-2\pi ct,\qquad 0\le t\le1,\\
 I_z(t)&=\int_0^t\log|1-e^{-2\pi i(z+u)}|\,du,\qquad
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\\
 \lambda&=2\pi\{(-c)_++d_+\}\le22\pi/125<14/25.
\end{split}                                                       \tag{4}
\]
Integrals at zeros use their original continuous limits.
The continuous last rate is exactly \(E(1)=\lambda\).

**Theorem.** Under (1),
\[
 \boxed{\quad
 \max_{1/2\le t\le1}E(t)=\max\{E(1/2),\lambda\}.
 \quad}                                                          \tag{5}
\]
Consequently, for every \(\tau>0\), uniformly on the indicated
compact parameter set and at both parities,
\[
 \boxed{\quad
 \sum_{j=\lceil N/2\rceil}^{N-1}|R_{j,N}|
 \le C_\tau N^{B_\tau}
      \exp N\{\max(E(1/2),\lambda)+\tau\}.
 \quad}                                                          \tag{6}
\]
The endpoint \(t=1\) controls the actual last index with its
original uniform endpoint error; it is not an added row \(j=N\).
No finite half or last value is divided out.

## 2. Reflection and the two radial savings

Use the original primitive
\[
 G_H(u)=\Re g(u-iH),\qquad H\ge0,\qquad
 G'_H(u)=\log|1-e^{-2\pi H-2\pi iu}|.
\]
It is odd and one-periodic, and \(J\le G_H\le0\) on
\([0,1/2]\). Its derivative is even and increases with
distance from the nearest integer on that interval.
The exact reciprocal-radius identity in
[the reflection source](research_mixed_right_tail_reflection.md),
equations (3)--(4), gives
\[
\begin{split}
 \Phi(v)&:=E(1-v)-E(1)\\
 &=G_{|c|}(x-v)-G_{|c|}(x)
   +G_{|d|}(q-v)-G_{|d|}(q)+3J(v)-\lambda v,
                         \qquad0\le v\le1/2.                   \tag{7}
\end{split}
\]
This algebraic identity holds throughout the real half period;
the narrower angular domain in that source is not used to
derive it. Both positive-height numerator means and the
incoming chirp occur in the displayed \(\lambda\).

The centered-arc minimum and the all-angle leg inequality
of [the sign-class theorem, Lemma 1](research_mixed_all_angle_high_row_sign_class.md)
give respectively
\[
\begin{split}
 \Phi(v)&\le3J(v)-2G_{|c|}(v/2)-2G_{|d|}(v/2)-\lambda v,\\
 \Phi(v)-\Phi(1/2)&\le J(v)+\lambda(1/2-v).
\end{split}                                                       \tag{8}
\]
The arcs lie in \([-1/2,1/2]\). Continuity includes \(x,q=0,1/2\).
The second inequality is obtained by applying the leg inequality
separately to the two radii, before discarding either leg.

Put \(B(v)=3J(v)-4J(v/2)\), and write
\[
 \lambda_1=2\pi(-c)_+,\qquad\lambda_2=2\pi d_+,\qquad
 \lambda=\lambda_1+\lambda_2.
\]
The original radial derivative, also derived in equations
(23)--(24) of the
[bounded-drift high-row proof](research_mixed_complete44_two_early_angles_high_rows.md), is
\[
 \partial_HG_H(u)=\frac\pi2-\pi u
       -\arctan\{\tanh(\pi H)\cot(\pi u)\}.
\]
Its principal real arctangent retains the original lift.
Using \(\arctan t\le t\), \(\tanh t\le t\), and
\(\cot t\le1/t\), integration gives
\[
 2\{G_H(v/2)-J(v/2)\}
                  \ge\pi H(1-v)-\frac{2H^2}{v}.                \tag{9}
\]
If \(c\le0\), use \(H=-c=\lambda_1/(2\pi)\) on the first
leg; if \(c>0\), discard its nonnegative radial saving and
use \(\lambda_1=0\). Treat the second leg with \(H=d\)
when \(d\ge0\), and discard it otherwise. Thus (8)--(9) imply
\[
\begin{split}
 \Phi(v)
 &\le B(v)-\frac{\lambda(1+v)}2
                    +\frac{\lambda_1^2+\lambda_2^2}{2\pi^2v}\\
 &\le B(v)-S(\lambda,v),\qquad
 S(\lambda,v)=\frac{\lambda(1+v)}2-\frac{\lambda^2}{2\pi^2v}.
\end{split}                                                       \tag{10}
\]
The inequality \(\lambda_1^2+\lambda_2^2\le\lambda^2\) only
weakens a saving already retained from both actual radii.
The drift has not been varied independently of the heights.

## 3. Small indices and the shallow-drift case

For \(0<u\le47/400\), the sine bound and
\(\log(1-t)\ge-t/(1-t)\) give
\[
 \log(2\sin\pi u)\ge\log(2\pi u)-\frac{\pi^2u^2}{5}.
                                                                    \tag{11}
\]
Indeed \((\pi u)^2<1\) on this interval, so the same proof
as the bounded-drift source applies on the larger interval.
Combining (11) with \(\sin\pi u\le\pi u\) and integrating,
\[
 B(v)\le v\{\log(8\pi v)-1\}+\frac{\pi^2v^3}{30},
                        \qquad0<v\le v_0:=47/200.               \tag{12}
\]
For \(0<v\le1/10\), the written witness in that source gives
\[
 B(v)<-\frac7{150}v.
                                                                    \tag{13}
\]
For completeness, \(\log(4\pi/5)<19/20\), since
\[
 e^{19/20}>
 1+\frac{19}{20}+\frac{361}{800}+\frac{6859}{48000}
 =\frac{122119}{48000}>\frac{88}{35}>\frac{4\pi}{5}.
\]
Use \(\pi^2<10\) in (12). From the first line of (8) and
\(G_H\ge J\), all these rows satisfy \(\Phi(v)<0\).

If \(0\le\lambda\le7/20\), the same original sine bound gives
\[
 J(1/10)\le\tfrac1{10}\{\log(\pi/5)-1\}<-7/50.
                                                                    \tag{14}
\]
Here \(\pi/5<2/3\) and \(\log(3/2)>2/5\).
Convexity of \(J\) on \([1/10,1/2]\), with \(J(1/2)=0\),
therefore gives
\[
 J(v)<-\tfrac7{20}(1/2-v),\qquad1/10\le v<1/2.
\]
The second line of (8) pays this whole range by the half rate.
This finishes the shallow-drift case.

## 4. The larger drift: a convex scalar bound on \([1/10,v_0]\)

Suppose \(7/20\le\lambda\le14/25\). By (10)--(12),
\(\pi^2<10\), and \(\pi^2>48/5\),
\[
 \Phi(v)<F_\lambda(v):=
 v\{\log(8\pi v)-1\}+\frac{v^3}{3}
 -\frac{\lambda(1+v)}2+\frac{5\lambda^2}{96v},
                      \quad1/10\le v\le v_0.                   \tag{15}
\]
This function is strictly convex in \(v\):
\[
 F_\lambda''(v)=\frac1v+2v+\frac{5\lambda^2}{48v^3}>0.
                                                                    \tag{16}
\]
It suffices to pay its two endpoints, uniformly in \(\lambda\).

At \(v=1/10\), its first two terms are negative by the same
calculation as (13). The subtracted saving
\[
 \frac{\lambda(1+v)}2-\frac{5\lambda^2}{96v}
\]
is concave in \(\lambda\). At the two allowed endpoints it
is respectively
\[
 \frac{77}{400}-\frac{49}{768}>\frac18,\qquad
 \frac{77}{250}-\frac{49}{300}=\frac{217}{1500}>\frac18.
                                                                    \tag{17}
\]
Hence \(F_\lambda(1/10)<0\).

At \(v=v_0=47/200\), use
\[
 \log(47\pi/25)<89/50.                                           \tag{18}
\]
A finite positive-series witness is
\[
 e^{3/2}>\frac{22925}{5120},\qquad
 e^{7/25}>1+\frac7{25}+\frac{49}{1250}+\frac3{1000}
          =\frac{6611}{5000}.
 \tag{19}
\]
The first is the sum through degree six, and the cubic term
\(343/93750\) in the second exceeds \(3/1000\).
Their product exceeds \(1034/175>47\pi/25\); the first
cross-product difference is \(52105625>0\).
Since \(3/2+7/25=89/50\), this proves (18).
Consequently the first two terms in (15) satisfy
\[
 v_0\{\log(8\pi v_0)-1\}+v_0^3/3
 <\frac{1833}{10000}+\frac{103823}{24000000}
 <\frac{47}{250}.                                               \tag{20}
\]
The last strict difference has numerator \(8977\) over
\(24000000\).

The subtracted saving is again concave in \(\lambda\).
At \(\lambda=7/20\) it equals
\[
 \frac{1729}{8000}-\frac{245}{9024}>\frac{47}{250};
                                                                    \tag{21}
\]
the comparison reduces to \(9\cdot9024>245\cdot320\).
At \(\lambda=14/25\), it equals
\[
 \frac{1729}{5000}-\frac{49}{705}>
                    \frac13-\frac7{100}>\frac{47}{250}.         \tag{22}
\]
Thus \(F_\lambda(v_0)<0\) throughout the whole drift interval.
Convexity (16) and the two endpoint inequalities prove
\[
                         \Phi(v)<0,\qquad1/10\le v\le v_0.
                                                                    \tag{23}
\]
These rows are bounded by their literal last rate.

## 5. The remaining indices are bounded by the half rate

The original Catalan witness in
[the half-interval packet, equation (21)](research_repeated_two_block_half_interval_packet.md)
gives
\[
                          -J(1/4)>63/440.
                                                                    \tag{24}
\]
Also \(2\sin(47\pi/200)>4/3\). To see this without evaluating
a trigonometric value, use \(\pi>25/8\) and
\[
 \sin(47\pi/200)>
 \frac{47}{64}-\frac{(47/64)^3}{6}>\frac23.
                                                                    \tag{25}
\]
The last numerator comparison is \(3153747>3145728\).
Since \(J'\) increases up to \(1/4\),
\[
 -J(v_0)>
 \frac{63}{440}+\left(\frac14-\frac{47}{200}\right)\log(4/3)
 >\frac{63}{440}+\frac3{700}=\frac{2271}{15400}.
                                                                    \tag{26}
\]
Here \(\log(4/3)>2/7\) is the first positive
\(\operatorname{arctanh}\) term.
This pays the entire permitted drift:
\[
 \frac{2271}{15400}>
 \frac{12826}{87500}>
 \frac{22\pi}{125}\left(\frac12-\frac{47}{200}\right).
                                                                    \tag{27}
\]
The first cross-product difference is \(1192100>0\);
the second uses \(\pi<22/7\).
Convexity of \(J\), its value zero at \(1/2\), and (27)
imply
\[
 J(v)+\lambda(1/2-v)<0,\qquad v_0\le v<1/2.
\]
Apply the second line of (8).
Together with Sections 3--4 and \(\Phi(0)=0\), this proves
(5) for every height and angle in (1).

## 6. All finite rows, parameters and remaining scope

Apply the zero-safe finite-row proof in Section 5 of the
bounded-drift theorem to the literal products (3). On any
fixed compact set satisfying (1), regularize each numerator
logarithm by
\(\log(|1-e^{-2\pi i(a+t)}|+\epsilon)\), and likewise for \(b\).
For fixed \(\epsilon>0\), the Riemann-sum upper errors are
uniform. The integrated excess tends uniformly to zero as
\(\epsilon\to0\), including all real-angle and height-zero
boundaries: the possible zeros are simple and have the
same integrable local bound. The denominator retains its
uniform \(O(\log N)\) error through every \(j<N\).
The original \(X^{-j}\) contributes exactly the chirp in (4).
Thus each row is bounded by its rate with any prescribed
tolerance and a polynomial factor. Apply (5) and sum fewer
than \(N\) rows to obtain (6).

Both parity endpoints and any half-grid change by \(O(1)\)
rows are included. No additional coefficient-extraction
factor \(N\) belongs to this row sum. Outside cap factors,
both complete Fourier alternatives, selected monomials and
the original halfweight allocations may be multiplied on
both sides without change, including at their zeros.

In particular (6) supplies the first own-four high block
when its output is \(q+i/100\), \(0\le q\le1/2\), and its
incoming first height is any height from the actual \(c_1\)
through zero or \(1/100\). It does not pay the remaining
half or last rate against \(\Lambda_{123}\), prove a
complete conditional-contour estimate, or complete a
selected second-coordinate connection.

## Direct source versions

| Source | Direct implication | SHA-256 |
|---|---|---|
| research_mixed_right_tail_reflection.md | exact arbitrary-height reciprocal reflection and radial primitives | e3928f2d9549159f6955c654b202dc87198137f4cfdb80f85151af567a976ce1 |
| research_mixed_all_angle_high_row_sign_class.md | all-angle leg inequality, including zero-safe boundary limits | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| research_mixed_complete44_two_early_angles_high_rows.md | original radial-saving formula, small-index witnesses and finite-row proof | b088d7b6e388f65f3a96e9176f810cfd0936cb31f425e47fcd9808c6dcb81c8d |
| research_repeated_two_block_half_interval_packet.md | written Catalan bound (21), with \(b_2=-4J(1/4)\) | fba89dd103a469bbe6346089f763331ac1e8322ca8b0715cf039de8c5028bae3 |
