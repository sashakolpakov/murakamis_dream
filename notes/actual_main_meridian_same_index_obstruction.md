# Why a moving multiplication trace cannot be bounded at the same indices

1 November 2026.

A product junction in a Conway calculation multiplies several tangle operators before taking their trace. After expanding those operators in the complete Newton basis, one obtains traces of products of basis polynomials. A tempting estimate would bound each moving trace by a polynomial in the level times its complete trace at exactly the same basis indices. This estimate is false, even for a junction with nine incident factors and a strictly positive complete trace.

Here “high” refers to a Newton basis index greater than \(\lfloor(N-1)/2\rfloor\). It does not refer to the physical color of an auxiliary crossing circle. The example has exactly one high index and satisfies the complete pairwise support inequalities. Its moving-to-complete ratio grows exponentially along both level parities.

The proof below keeps the exact quotient trace, including derivatives at repeated roots. The conclusion concerns an individual tensor entry, not a knot invariant or a whole tangle contraction. The [reflected Fourier estimate](actual_main_meridian_high_fourier_reflection.md) and the [general component comparison](actual_main_meridian_general_component_comparison.md) explain how the full source can still be controlled: they compare the change in the trace with a different, reflected index and retain the neighboring branch profiles.

## 1. Conventions and the family

Let \(\mathcal T_N\) be the monic normalized Chebyshev polynomial characterized by \(\mathcal T_N(u+u^{-1})=u^N+u^{-N}\). The level is \(N\), the complete meridian is \(s=0\), and the moving meridian is \(M=q^s\). Set \(S_0=B_0=1\). Use the fixed complete Newton polynomials
\[
\begin{gathered}
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad
 c_j=2\cos((2j+1)\pi/N),\\
 S_n=\prod_{r=1}^n2\sin(\pi r/N),\qquad
 B_n(z)=\prod_{j=0}^{n-1}(c_j-z),\qquad e_n=B_n/S_n^2,\\
 P_0(z)=\mathcal T_N(z)+2,\qquad
 P_s=P_0+\Delta_s,\qquad \Delta_s=2\cos(2\pi s)-2,\\
 \phi_s(F)=(-1)^dN^2[z^d]\operatorname{rem}_{P_s}F.
\end{gathered}
\tag{1}
\]
The node index runs over \(0\le j\le d\), and the basis consists of \(e_0,\ldots,e_d\). Here \(\operatorname{rem}_{P_s}F\) is the unique remainder of degree less than \(N\) after division by the monic polynomial \(P_s\), and \([z^d]\) extracts its coefficient of \(z^d\). All products in the trace are ordinary polynomial products followed by this single exact quotient reduction. Thus repeated-root derivative data are retained, rather than replacing the trace by evaluations only.

For an integer \(a\ge7\), take
\[
             N=5a+1,\qquad d=5a,\qquad h=4a,
             \qquad \mathcal Z_a(s)=\phi_s(e_h e_a^8).
\tag{2}
\]
There are nine factors. Exactly one index, \(h\), is high. The other eight indices equal \(a=d-h\). Each high/low pair has sum \(d\), each low/low pair has sum \(2a<d\), and the total is \(12a>d\). These are the complete pairwise and total-sum support conditions; a tuple satisfying them is called complete-admissible here. Its support is on a pair-equality face; no assertion of strict interior admissibility is being made.

We prove an exact identity
\[
       \mathcal Z_a(s)=\mathcal Z_a(0)+(-1)^a\Delta_s\mathcal B_a,
       \qquad \mathcal Z_a(0)>0,\quad \mathcal B_a>0,
\tag{3}
\]
and the explicit lower bound
\[
 \boxed{\displaystyle
 \frac{\mathcal B_a}{\mathcal Z_a(0)}
       \ge\frac1{3(5a+1)}
                         \left(\frac{25000}{6561}\right)^a.}
\tag{4}
\]
For every fixed \(s\) with \(\Delta_s\ne0\), (3)–(4) imply
\[
 \frac{|\mathcal Z_a(s)|}{\mathcal Z_a(0)}
       \ge \frac{|\Delta_s|}{3(5a+1)}
                          \left(\frac{25000}{6561}\right)^a-1.
\tag{5}
\]
In particular no power of \(N\), even with a constant depending on a fixed disk \(|s|\le R<1\), can bound this ratio for any \(R>0\). One may choose one fixed nonzero real or imaginary \(s\) in that disk. As \(a\) varies, the levels in (2) include both parities. For even \(a\) and imaginary nonzero \(s\), both summands in (3) are positive; (5) does not require this favorable sign.

## 2. An exact complementary-index identity

The reflection of the complete nodes gives
\(B_N=(-1)^NP_0\) and
\(B_hB_{a+1}=B_N\), since \(h+a=d\). Also
\(S_hS_a=N\). Consequently
\[
       e_he_a=\frac{(-1)^d}{N^2}\frac{P_0(z)}{z-c_a}.
\tag{6}
\]
The denominator on the right divides \(P_0\); the expression is a polynomial.

Put \(F=e_a^7\) and
\[
                         D(z)=\frac{F(z)-F(c_a)}{z-c_a}.
\tag{7}
\]
Then \(\deg D=7a-1<2N-1\). A single division by \(P_0\) has quotient degree at most \(N-2\). Replacing \(P_0\) by \(P_0+\Delta_s\) therefore does not change the top trace coefficient:
\[
                              \phi_s(D)=\phi_0(D).
\tag{8}
\]
The same degree argument gives \(\phi_s(e_he_a)=1\). Multiplying (6) by \(F\), using (7), and reducing \(P_0=-\Delta_s\) proves
\[
        \mathcal Z_a(s)
           =F(c_a)-\Delta_s\frac{(-1)^d}{N^2}\phi_0(D).
\tag{9}
\]
There is no quadratic or higher term in \(\Delta_s\). The exact complete value is
\[
                  \mathcal Z_a(0)=F(c_a)
                       =\left(\frac{S_{2a}}{S_a^2}\right)^7>0.
\tag{10}
\]
Here \(B_a(c_a)=S_{2a}\), obtained by multiplying
\(c_r-c_a=4\sin((a+r+1)\pi/N)\sin((a-r)\pi/N)\) for \(0\le r<a\).

## 3. Removing the repeated upper nodes

A divided difference records polynomial interpolation at several points; when points repeat, it records derivatives there as well. For a real node multiset \(\Lambda=(\lambda_0,\ldots,\lambda_m)\), including repetitions, write \(F[\Lambda]\) for the Hermite divided difference. It has the algebraic description
\[
        F[\Lambda]=[z^{-1}]
                   \frac{F(z)}{\prod_{j=0}^m(z-\lambda_j)},
\tag{11}
\]
where the coefficient is in the Laurent expansion at infinity. This is the top coefficient of the polynomial remainder, so (11) requires no limiting choice of distinct roots.

Let \(\Lambda_N=(c_0,\ldots,c_d)\), the roots of \(P_0\) with their actual multiplicities. Equations (7) and (11) give
\[
 \frac{(-1)^d}{N^2}\phi_0(D)
       =D[\Lambda_N]=F[c_a,\Lambda_N].
\tag{12}
\]
The last equality follows by writing \(F=(z-c_a)D+F(c_a)\); the constant term divided by a monic polynomial of degree \(N+1\) has no \(z^{-1}\) coefficient.

The nodes \(c_0,\ldots,c_{a-1}\) are all larger than \(c_a\), and each occurs twice in \(\Lambda_N\). Cancel their quadratic factor \(B_a(z)^2\) between numerator and denominator in (11). Since \(F=B_a^7/S_a^{14}\), this gives
\[
 F[c_a,\Lambda_N]
   =G[\Lambda_a],\qquad
 G(z)=\frac{B_a(z)^5}{S_a^{14}}.
\tag{13}
\]
The remaining multiset \(\Lambda_a\) consists of the \(N-2a=3a+1\) uncanceled complete nodes, together with the one extra \(c_a\). It therefore has \(3a+2\) nodes, every one at most \(c_a\), and the divided-difference order is
\[
                                  m=3a+1.
\tag{14}
\]
This cancellation includes repeated-node derivatives exactly.

Put \(\delta_r=c_r-c_a>0\) for \(0\le r<a\). On the entire interval below \(c_a\),
\[
            G(c_a-v)=\frac1{S_a^{14}}
                          \prod_{r=0}^{a-1}(\delta_r+v)^5,
                         \qquad v\ge0.
\tag{15}
\]
Every coefficient in this polynomial in \(v\) is positive. Hence
\((-1)^mG^{(m)}(z)>0\) for \(z\le c_a\), and its magnitude is at least its magnitude at \(c_a\).

The real divided-difference formula is
\[
 G[\lambda_0,\ldots,\lambda_m]
  =\int_{\substack{t_j\ge0\\\sum t_j=1}}
         G^{(m)}\!\left(\sum t_j\lambda_j\right)\,dt,
\tag{16}
\]
with simplex measure of total mass \(1/m!\). It follows by repeated use of the fundamental theorem of calculus and remains valid for repeated nodes by continuity. Since all the nodes in (13) are at most \(c_a\), (15)–(16) prove
\[
 \operatorname{sign}G[\Lambda_a]=(-1)^m,
 \qquad |G[\Lambda_a]|
               \ge\frac{|G^{(m)}(c_a)|}{m!}.
\tag{17}
\]
Equations (9), (12) and (14) now give (3), with
\(\mathcal B_a=|G[\Lambda_a]|\): the coefficient of \(\Delta_s\) has sign
\(-(-1)^{3a+1}=(-1)^a\).

## 4. An explicit exponential lower bound

Let \(L_a=c_0-c_a\), so \(0<\delta_r\le L_a\). The coefficient of \(v^m\) in (15), divided by \(F(c_a)\), is
\[
 \frac1{B_a(c_a)^2}
     e_m(\delta_0^{-1},\ldots,\delta_0^{-1},
                     \ldots,\delta_{a-1}^{-1},\ldots,\delta_{a-1}^{-1}),
\tag{18}
\]
where each reciprocal appears five times and \(e_m\) in this formula denotes the elementary symmetric polynomial, rather than a Newton basis element. Each of its \(\binom{5a}{m}\) summands is at least \(L_a^{-m}\), while \(B_a(c_a)^2\le L_a^{2a}\). Therefore
\[
          \frac{\mathcal B_a}{F(c_a)}
             \ge \binom{5a}{3a+1}\,L_a^{-(5a+1)}.
\tag{19}
\]
For \(a\ge7\),
\[
 \frac{2a+1}{5a+1}\le\frac5{12},\qquad
 c_a\ge2\cos\frac{5\pi}{12}>\frac12,
                      \qquad L_a<\frac32.
\tag{20}
\]
The middle term of a binomial distribution with \(5a\) trials and success probability \(3/5\) is a mode. Its mass is at least \(1/(5a+1)\). Thus
\[
 \binom{5a}{3a}\ge\frac1{5a+1}
                  \left(\frac{5^5}{3^3 2^2}\right)^a,
 \qquad
 \binom{5a}{3a+1}=\binom{5a}{3a}\frac{2a}{3a+1}
                              \ge\frac12\binom{5a}{3a}.
\tag{21}
\]
Insert (20)–(21) into (19). The remaining factor is
\[
 \frac{1}{2(5a+1)}
   \left(\frac{5^5}{3^3 2^2}\right)^a
   \left(\frac23\right)^{5a+1}
 =\frac1{3(5a+1)}\left(\frac{25000}{6561}\right)^a,
\tag{22}
\]
which proves (4). In particular, for any fixed \(\Delta_s\ne0\),
\[
 \liminf_{a\to\infty}\frac1{5a+1}
       \log\frac{|\mathcal Z_a(s)|}{\mathcal Z_a(0)}
                  \ge\frac15\log\frac{25000}{6561}>0.
\tag{23}
\]

## 5. What the obstruction rules out

The family disproves a uniform pointwise estimate
\(|\phi_s(\prod e_i)|\le N^{C_R}\phi_0(\prod e_i)\)
on all complete-admissible tuples of a fixed valence. Allowing a prefactor depending on \(R\) does not help. There is a strictly positive complete denominator, exactly one high input, and an explicit exponential lower bound. The same construction applies at both even and odd levels.

The indices lie on complete pair-equality faces. The example does not disprove an estimate restricted to a fixed strict compact interior window. More fundamentally, a tensor entry does not include the neighboring physical coefficient profiles or the sum over shared indices. Those additional factors and correlations are part of the whole Conway source. This is therefore not a counterexample to a knot-volume theorem.

The useful replacement is a bound on the difference between the moving and complete traces. In the exact Fourier formula for that difference, the first Fourier contribution cancels. The [reflected Fourier theorem](actual_main_meridian_high_fourier_reflection.md) bounds the remaining contribution by a complete trace with the high index \(h\) replaced by the low index \(d-h\), with a strict exponential improvement on the relevant regular windows. It does not assert the false comparison at unchanged indices proved impossible here.

The [general component theorem](actual_main_meridian_general_component_comparison.md) combines this reflected estimate with exact Frobenius contraction and the original coupled positive action. Reflection can fuse two junctions in a comparison tree; the geometric pressure of that tree is no greater than the original pressure. These comparison operations bound correction terms without changing the actual knot, the original finite source, or its marked filling action. Thus the obstruction explains why that proof retains whole contractions instead of using an estimate on each unchanged tensor entry.
