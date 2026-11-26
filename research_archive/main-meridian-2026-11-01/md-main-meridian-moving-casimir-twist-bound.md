# Polynomial control of moving Casimir twist blocks, and the first resonance obstruction

Private proof, 31 October 2026. No frozen or public file is changed.

This note isolates a genuine local part of the main-meridian problem. Fixed integral twist blocks have polynomially bounded canonical Casimir representatives on every compact disk before the first ordinary-color resonance. Multiplication in the moving Casimir algebra also has polynomial cost. The physical crossing itself gives an exact obstruction to extending that particular norm through the first ordinary resonance. These are statements about the actual crossing, not auxiliary-circle color packets.

## 1. The actual moving algebra and crossing values

Use the root \(q=e^{\pi i/N}\), \(Q=q^2\), and
\(\alpha=N-1+s\). Then
\[
 M=q^s,\quad Y=Q^s,\quad U=Y^N=e^{2\pi is}.
\tag{1}
\]
Let \(\mathcal T_N(z)=2T_N(z/2)\), where \(T_N\) is the usual first-kind Chebyshev polynomial. The actual equal-color tensor Casimir has generic algebra
\[
 A_{N,s}=\mathbb C[z]/P_{N,s}(z),\qquad
 P_{N,s}=\mathcal T_N+U+U^{-1}.
\tag{2}
\]
Its nodes and stripped checked-crossing values are
\[
 t_j=q^{-2j-1}Y,\quad c_j=t_j+t_j^{-1},\qquad
 \lambda_j=(-1)^j q^{j(j+1)}Y^{-j},\quad 0\le j<N.
\tag{3}
\]
These are the exact source formulas in `meridian_casimir_source.md`, Section 1, obtained from the original highest vectors and finite R. For a fixed integer \(n\), let \(r^{[n]}_{N,s}\) be the degree-\(<N\) polynomial with values \(\lambda_j^n\) at distinct nodes. Thus it represents the actual stripped crossing power \(B_N(M)^n\) at generic color, including negative powers. No eigenvalue-modulus approximation is used.

## 2. Bound before the first ordinary resonance

**Proposition.** For every \(0<R<1\) and fixed integer \(n\), the coefficients of \(r^{[n]}_{N,s}\) extend holomorphically to \(|s|<1\), and
\[
 \sup_{|s|\le R}\sup_{z\in[-2,2]}
 \bigl(|r^{[n]}_{N,s}(z)|+
                 |\partial_zr^{[n]}_{N,s}(z)|\bigr)
       \le C_{R,n}N^4.
\tag{4}
\]
The constants are independent of level and its parity. The same bound controls the complete full-Hermite norm, because all complete double nodes lie in \([-2,2]\), with the odd simple node included.

First suppose \(\sin(2\pi s)\ne0\). Differentiating
\(\mathcal T_N(t+t^{-1})=t^N+t^{-N}\), and using \(t_j^N=-U\), gives
\[
 P'_{N,s}(c_j)=
       -\frac{N(U-U^{-1})}{t_j-t_j^{-1}}.
\tag{5}
\]
Hence the exact Lagrange formula is
\[
 r^{[n]}_{N,s}(z)=
 -\frac1{N(U-U^{-1})}
 \sum_{j=0}^{N-1}\lambda_j^n(t_j-t_j^{-1})
         \frac{P_{N,s}(z)}{z-c_j}.
\tag{6}
\]
The quotient in (6) is a polynomial. Since \(P(c_j)=0\), it is also
\( [\mathcal T_N(z)-\mathcal T_N(c_j)]/(z-c_j)\).

For bounded \(|s|\), the nodes lie in the closed Bernstein ellipse with angular height \(2\pi|\operatorname{Im}s|/N\). That ellipse is convex and contains \([-2,2]\), so every line segment from a real \(z\) to a node stays in an ellipse of height \(2\pi r/N\) for \(|s|\le r\). On it,
\[
 |\mathcal T_N'|\le C_rN^2,\qquad
 |\mathcal T_N''|\le C_rN^4.
\tag{7}
\]
For the first bound use \(\mathcal T_N'=N U_{N-1}(z/2)\) and the N-term exponential formula for \(U_{N-1}(\cos w)\). For the second expand that U-polynomial into first-kind Chebyshev terms and differentiate; the sum of their squared degrees is \(O(N^3)\), before the factor N. Their exponential heights are bounded by \(e^{2\pi r}\).

Integrating the first derivative along the segment bounds the quotient in (6) by \(C_rN^2\); differentiating that integral with respect to \(z\) bounds its derivative by \(C_rN^4\). Also \(|\lambda_j^n|\le e^{2\pi r|n|}\) and \(|t_j-t_j^{-1}|\le C_r\). Thus
\[
 \sup_{[-2,2]}(|r^{[n]}|+|\partial_zr^{[n]}|)
       \le \frac{C_{r,n}N^4}{|\sin(2\pi s)|}.
\tag{8}
\]

It remains to justify removal of the collisions inside \(|s|<1\), rather than dividing by their zero. Distinct nodes coincide only when
\[
                j+l+1-2s=mN\quad(m\in\mathbb Z).
\tag{9}
\]
Inside this disk collisions occur only at \(s=0,1/2,-1/2\). For distinct \(j,l\), their index bounds force \(m=1\) at each of these points. The only apparent alternative at \(s=1/2\) is \(j=l=0\), which is not a collision of distinct nodes. At such a paired collision,
\[
 \frac{\lambda_l}{\lambda_j}
     =(-1)^{l-j}q^{(l-j)(j+l+1-2s)}=1.
\tag{10}
\]
The difference \(c_j-c_l\) has a simple zero, and \(\lambda_j^n-\lambda_l^n\) vanishes there. Their divided difference is therefore holomorphic. All other nodes are separated except for disjoint pairs. Replacing each such pair by its value and divided-difference interpolation rows gives a holomorphic interpolation matrix with invertible confluent limit. Its degree-\(<N\) coefficients have removable singularities. This proves holomorphy through all three points, including both level parities and the unpaired endpoint nodes.

Choose a radius \(r\in(R,1)\) with \(r\ne1/2\). The circle \(|s|=r\) misses all zeros of \(\sin(2\pi s)\). Apply the maximum principle in s, separately to the polynomial and its z derivative for every real z, to (8). This proves (4).

Restoring the full common Cartan factor or its zero-framing correction changes (4) by a bounded scalar on each such s-disk for a fixed twist power. Indeed the complete scalar is a unit, and its ratio to that value has exponent \(O_{R,n}(1)\); the quadratic \(s^2/N\) term is retained. The assertion is not an operator-norm bound for evaluating a polynomial in the physical tensor matrix. It is a bound in the canonical polynomial/full-Hermite norm used by the complete-source estimates.

## 3. Products in the moving algebra do not cost an exponential

For a polynomial \(f\) of degree at most \(2N-2\), write its Chebyshev expansion as
\(f=a_0+\sum_{j=1}^{2N-2}a_j\mathcal T_j\). Its coefficients are bounded by a constant times \(\|f\|_{[-2,2]}\), by their cosine integral. In the algebra (2), putting \(c=U+U^{-1}\),
\[
 \mathcal T_N\equiv-c,\qquad
 \mathcal T_{N+k}\equiv-c\mathcal T_k-\mathcal T_{N-k}
                    \quad(1\le k\le N-2).
\tag{11}
\]
This is the exact product identity
\(\mathcal T_N\mathcal T_k=\mathcal T_{N+k}+\mathcal T_{N-k}\).
It follows that the canonical remainder satisfies
\[
 \|f\bmod P_{N,s}\|_{[-2,2]}
       \le C_RN\|f\|_{[-2,2]}
                    \quad(|s|\le R),
\tag{12}
\]
for any fixed R, with no exclusion of a resonance. Its derivative costs only another factor \(O(N^2)\) by the polynomial Markov inequality (or the same cosine expansion).

In particular, for two canonical representatives, multiplication and reduction have polynomial cost in the supremum-plus-derivative norm. The complete Hermite norm is polynomially equivalent to this norm on degree-\(<N\) representatives: the reverse inequality is the established complete Hermite interpolation bound, and the forward inequality follows by sampling. Thus (12) also gives a polynomial-cost multiplication estimate in that full norm. Iterating a fixed number of products remains polynomial. No positivity, scalar source projection, or deletion of a derivative direction is used here.

This local algebra bound does not supply the physical turn between same-oriented and oppositely oriented color pairs. That turn is the remaining typed source map; the two algebras cannot be identified merely because their complete fibers agree.

## 4. The first ordinary resonance genuinely breaks the polynomial chart

For the fundamental crossing, at \(s=1\) one has
\[
 c_0=c_1=q+q^{-1},\qquad \lambda_0=1,\quad\lambda_1=-1.
\tag{13}
\]
Consequently no polynomial with coefficients holomorphic through this point can take the prescribed two values. More explicitly,
\[
 c_0-c_1=q^{-3}(Q-1)(Y-Q^2/Y),\qquad
 \lambda_0-\lambda_1=1+Q/Y.
\tag{14}
\]
Since \(dY/ds=(2\pi i/N)Y\),
\[
 \left.\frac{d}{ds}(c_0-c_1)\right|_{s=1}
     =\frac{4\pi i}{N}(q-q^{-1})
     =-\frac{8\pi\sin(\pi/N)}N.
\]
Therefore the divided difference has the exact principal part
\[
 \frac{\lambda_0-\lambda_1}{c_0-c_1}
   =-\frac{N}{4\pi\sin(\pi/N)}\frac1{s-1}+O_N(1).
\tag{15}
\]
For real s near one, the nodes are real and lie in \([-2,2]\). Integrating the polynomial derivative between them shows that its supremum must be at least the modulus of (15). The polynomial chart thus has a genuine pole at each fixed level, not merely a worsening asymptotic constant.

The physical finite crossing matrix is regular in s, as is every actual knot cut scalar. At this ordinary-color point the Casimir no longer generates the relevant crossing action by a regular polynomial chart. The pole of its generic representative cancels only after evaluation in the degenerating physical realization or after a different source adapter. It cannot be removed by imposing the complete Hermite norm alone. This obstruction concerns this representation and does not assert a pole of \(F_N\), a pole of its regular remainder, or failure of their possible scaled profiles.

An even power has equal values at the two nodes in (13); the fundamental-crossing obstruction must therefore not be asserted for every twist exponent. Proposition (4) applies uniformly to all fixed powers on the stated pre-resonance disk without needing such further case analysis.

## 5. Relation to the paired-sine insertion test

The actual figure-eight identity in `figure_eight_whole_source_identity.md` is
\[
 f_N(Y)=\sum_{n=0}^{N-1}
       \prod_{r=1}^{n}(Y+Y^{-1}-Q^r-Q^{-r}).
\tag{16}
\]
At \(Y=e^{z/N}\), each term divided by its positive complete value is exactly
\[
 \prod_{r=1}^{n}
 \left(1+\frac{\sinh^2(z/(2N))}{\sin^2(\pi r/N)}\right).
\tag{17}
\]
Thus a uniform paired-sine bound acts after the cancellations already eliminated by (16). It is qualitatively stronger than applying an absolute bound to the unreduced crossing paths.

The same Newton factors occur in the genuine whole five-crossing source, proved in `five_two_cyclotomic_transform_proof.md`, equation (1), but with the nontrivial coefficients
\(C_n(Q)=(-1)^nQ^{-n(n+3)/2}H_n(Q^{-n-1})\).
Its source is signed/complex. `actual_multichannel_newton_green_transport.md` proves exponential growth of some of those coefficients and retains a nonsharp absolute barrier. Consequently (17) alone cannot be pushed through that signed outer sum using positivity. Neither this source identity nor an equivalent paired insertion was found for every strict Conway tree in the current compiler notes.

The concrete local advance here is (4) and (12), with the exact chart obstruction (15). A whole main-meridian theorem still needs the physical typed turn/recoupling and an estimate of the resulting signed source, or an exact elimination analogous to (16) which exposes a controlled paired insertion before taking absolute values.
