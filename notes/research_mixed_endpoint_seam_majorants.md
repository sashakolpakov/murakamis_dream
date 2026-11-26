# Uniform seam collars for the original endpoint factors

Research deduction, 5 November 2026. Literal Newton majorants give a
strict cap-factor bound near the outgoing seam, uniformly in every
real ordinary color and every fixed ordinary derivative. The result
retains all private rows. It is not a global triangle estimate for a
coherent cap: the [type-four private-row obstruction](research_mixed_cap_private_row_triangle_obstruction.md)
excludes that stronger comparison at its own critical reference.

## 1. An elementary product collar

Put \(r=e^{-2\pi i/N}\), \(P_i=(r;r)_i\),
\(S_i=|P_i|\), and \(p_i(X)=(rX;r)_i\). Define
\[
 \omega(\delta)=\log(1+\delta/2)
             +\frac\delta2\log(1+2/\delta),\qquad \omega(0)=0.
                                                               \tag{1}
\]
For \(N\ge2\), \(0\le i<N\), and \(|X-1|\le\delta\),
\[
                         |p_i(X)|\le S_i e^{N\omega(\delta)}.
                                                               \tag{2}
\]
Indeed the ratio is at most
\(\prod_{j=1}^{N-1}(1+\delta/(2\sin(\pi j/N)))\).
Using \(\sin\pi t\ge2\min(t,1-t)\), symmetry, and the integral
upper bound for a decreasing function gives
\[
 \log\frac{|p_i(X)|}{S_i}
 \le2\sum_{j=1}^{\lfloor N/2\rfloor}
                   \log(1+\delta N/(4j))
 \le2N\int_0^{1/2}\log(1+\delta/(4t))\,dt
 =N\omega(\delta).                                      \tag{3}
\]
No denominator here vanishes. The overcount of the central factor
at an even level is harmless.

## 2. Both cap types, all ordinary colors

Retain the original \(U_{\epsilon,N}\) and \(H_N\) in
[torus composition, equation (21)](research_mixed_conditional_torus_composition.md).
Write \(b_2=2G_{\rm Cat}/\pi\) and
\(c=-3J(1/3)=2J(5/6)\). The existing scalar bounds give
\(b_2<73/125\) and \(c<1/3\). At every real ordinary color
\(w=-2\cos\theta\), the
[Newton derivative envelope](research_mixed_newton_color_tubes.md)
and its exact triangular identity imply
\[
 |\partial_w^k U_{\epsilon,N}(w,X)|
 \le \operatorname{poly}_k(N)e^{N\omega(\delta)}
 \sum_{0\le l\le i<N}
       \frac{S_i^{1-\epsilon}}{S_lS_{i-l}}
                         e^{N V_\theta(l/N)}
                  \quad(|X-1|\le\delta).                 \tag{4}
\]
Every sum in this note is the full indicated finite sum.

For \(\epsilon=0\), the factorial quotient in (4) has rate
\(J(s)-J(u)-J(s-u)\le c\) on \(0\le u\le s\le1\).
For completeness, at fixed \(s\in(0,1)\) it is strictly concave
in \(u\), since its second derivative is
\(-\pi\sin(\pi s)/(\sin(\pi u)\sin(\pi(s-u)))<0\).
Its maximum is at \(u=s/2\); differentiation in \(s\) then
gives \(\log(2\cos(\pi s/2))\), whose zero is \(s=2/3\).
The boundary value is zero. This proves the stated maximum.
For \(\epsilon=1\), use
\(\max_{[0,1]}(-J)=-J(1/6)=J(5/6)=c/2\).
Since \(V_\theta\le b_2\) on the entire row interval, including
its nonpositive upper half, (4) proves
\[
 |\partial_w^k U_{\epsilon,N}(w,X)|
     \le C_kN^{A_k}e^{N[b_2+c+\omega(\delta)]}
                         \quad(\epsilon=0,1).           \tag{5}
\]
The uniform factorial errors only contribute powers of \(N\).
These bounds hold at both level parities and do not require any
individual Newton factor to be nonzero.

Take \(\delta_0=1/1000\). Then
\(\omega(\delta_0)<9/2000\): use
\(\log(1+1/2000)<1/2000\) and \(\log2001<8\).
The latter follows, for example, from \(e>8/3\) and
\((8/3)^8>2001\). Consequently (5) gives the common bound
\[
 \boxed{\quad
 |\partial_w^k U_{\epsilon,N}(w,X)|
       \le C_kN^{A_k}e^{37N/40}
 \quad (|X-1|\le1/1000, -2\le w\le2).\quad}            \tag{6}
\]
The exact intermediate ceiling is
\(73/125+1/3+9/2000=5531/6000<37/40\).
For a complex ordinary-color tube of radius \(\tau\) about this
real interval, the undifferentiated bound adds at most
\(2\operatorname{arsinh}(\sqrt\tau/2)\le\sqrt\tau\) to
the rate, with the explicit prefactor in the Newton tube theorem.
Fixed derivatives on a smaller tube use Cauchy's formula. Outgoing
derivatives likewise use a smaller \(X\)-collar.

The [proved cap cuts](research_mixed_cap_real_cut_gaps.md) give
\(M_\epsilon>1\) at every correlated actual outgoing critical
image. Thus (6) is a strict loss of at least \(3/40\) relative to
that bare cap's critical rate. It does not yet compare the product
with an adjacent conditional factor.

## 3. The other endpoint and exact seam identities

The literal polynomial satisfies \(H_N(w,1)=1\), because every
\((1;r)_l\) with \(l\ge1\) vanishes. Its nearby absolute
majorant has a different, but still useful, bound. For \(l\ge1\),
(2) and \(2\sin(\pi l/N)\ge4/N\) give
\[
 \frac{|(Y;r)_l|}{S_l}
  =\frac{|1-Y|\,|p_{l-1}(Y)|}{S_l}
  \le\frac{\delta N}{4}e^{N\omega(\delta)}
                                  \quad(|Y-1|\le\delta).
                                                               \tag{7}
\]
The exact Newton envelope therefore implies, for every fixed \(k\),
\[
 |\partial_w^k H_N(w,Y)|
       \le C_kN^{A_k}e^{N[b_2+\omega(\delta)]}.           \tag{8}
\]
The \(l=0\) term is bounded separately by one. In particular the
ceiling at \(\delta_0\) is less than \(.589\). Formula (8)
does not assert that the nearby exponential rate tends to the exact
point value zero; no such conclusion is inferred from \(H_N(w,1)=1\).

The adjacent type-three identity
\[
                       C_{0,N}(1,Y)=N d_N(Y)              \tag{9}
\]
holds for arbitrary complex \(Y\), as proved in
[the boundary-strip theorem, Section 4](research_mixed_boundary_strip_bounds.md).
Its reversed identity is stated there too. These can be used with
the actual Fourier envelope, without setting the neighboring height
to zero. The hybrid cutoff at the seam itself is \(L_b(0)=1\);
the face \(x=\rho\), where it is zero, is a different point.

## 4. The calibrated comparison still required

For clarity consider an open word of length at least two, at complete
ordinary colors. Allocate half the first diagonal Fourier weight to
the cap and half to edge 2. Its reference cap phase is
\(\Phi_U=T_{\epsilon_1}-\epsilon_1 g/2\), and the allocated
edge phase is the original \(\phi_2\). Stationarity gives
\(\Phi_U'(r_1)+P_{2,a}=0\). At \(X_1=1\), its own Fourier
weight and selected monomial have zero logarithmic rate. Hence a
calibrated upper bound for this cap-plus-edge portion is
\[
 A_{\epsilon_1}+\mathcal E_2(1,z_2)
   -\Re\Phi_U(r_1)-\Re\phi_2(r_1,r_2)
   -\Re[P_{2,b}(z_2-r_2)],                               \tag{10}
\]
where \(A_0=A_1=b_2+c\), and
\(\mathcal E_2\) retains its actual remaining Fourier half and
all finite rows. The first-coordinate tangents cancel exactly;
the second-coordinate tangent is displayed rather than discarded.
Away from the exact seam, add the cap's actual half Fourier envelope
and selected half-rate as well. The neighboring hybrid height is
the physical one throughout.

The remaining middle completion must still be retained in comparing
(10), as in [finite boundary windows](research_mixed_open_finite_boundary_windows.md).
Neither the positive bare-cap reserve nor (9) proves the sign of
(10). In particular the larger open-reference boundary height ranges
cannot be replaced by the narrower cyclic reference rectangles.
This note proves only the explicit endpoint collars and identities;
it asserts no global open-source dominance or noncancellation.
