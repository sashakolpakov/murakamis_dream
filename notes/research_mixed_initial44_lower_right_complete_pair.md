# The complete initial four/four pair on the lower right horizontal

Private written proof, 10 November 2026. The entire original first
four/four pair is exponentially below its original geometric affine
rate while the first real coordinate runs from one half to seven
tenths at its actual negative height. The neighboring coordinate
remains on its full plateau at its own actual negative height.
The proof keeps the complete conditional polynomial: its physical
ends, both unweighted connecting sides, all four weighted sides,
and both horizontal aliases are included.

The height of the outermost private sampling rectangle is chosen
once, before the level, using compactness and a strict uniform alias
slope. No action value is evaluated in making that choice. This is
not a bound on the following height reset or the rest of the first
period.

## 1. Original source and statement

Use the actual references and exact source of
[the right-half theorem](research_mixed_initial44_right_half_interval.md):
\[
 a_*=a_0+ic,\quad b_*=b_0+id,\quad
 .246<a_0<.350,\quad -.078<c<-.020,\quad
 -.102\le d\le-.001 ,
\]
for a positive three/four word of length \(m\ge3\) beginning with
four and four. The independent targets are
\[
 a=x+ic,\quad 1/2\le x\le7/10,\qquad
 b=z+id,\quad z\in P=[11/50,9/20].
\tag{1}
\]
Let \(X=e^{-2\pi ia}\), \(Y=e^{-2\pi ib}\), and retain
\[
 K_N(w;a,b)=U_{1,N}(w,X)C_{1,N}(X,Y)d_N(X),
 \qquad |d_N(Y)|^{1/2}
\tag{2}
\]
with precisely the complete functions in that theorem. In particular
\[
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
 \frac{X^{-j}(q_NX;q_N)_j(q_NY;q_N)_j}{(q_N;q_N)_j^3},
 \qquad q_N=e^{-2\pi i/N}.
\tag{3}
\]
All Fourier forcing is retained. There is no selected first monomial.

Keep the original \(\Lambda(z)\), \(\kappa=1/2500000\),
\(\kappa_R=8\kappa/9\), and
\(\delta_R=\kappa(9/20-a_0)^2\).
**Theorem 1.** For every \(\tau>0\), uniformly on (1),
both parities and all real ordinary colors \(w\in[-2,2]\),
\[
 |K_N(w;a,b)|\,|d_N(Y)|^{1/2}
 \le C_\tau N^{A_\tau}
 \exp N\{\Lambda(z)-\kappa_R(z-b_0)^2-\delta_R+\tau\}.
\tag{4}
\]
The same estimate holds on sufficiently small fixed ordinary-color
disks with a separately reserved arbitrary allowance, and for fixed
derivatives on smaller disks. The literal horizontal integral with
its original \(N\,da\) measure and exterior scalar has the same
exponential bound.

No relative asymptotic for the whole \(C_{1,N}\) is asserted. Its
critical contribution and its other source terms are paid by
different calibrated inequalities.

## 2. The exact finite middle source at an arbitrary fixed height

Take the original cuts
\[
 L_N=\lfloor2N/25\rfloor+1,\quad M_N=\lceil N/2\rceil,\qquad
 \ell_N=(L_N-\tfrac12)/N,\quad b_N=(M_N-\tfrac12)/N.
\tag{5}
\]
The low and high rows are respectively \(j<L_N\) and \(j\ge M_N\).
The exact interpolant of the remaining rows is
\[
 T_N(s)=e^{2\pi iNas}\Pi_N(a+s)\Pi_N(b+s)
                          E_N(a)E_N(b)E_N(s)^3 .
\tag{6}
\]
Here \(\Pi_N\) is the original marked numerator factorial and
\(E_N=1/\Pi_N\) on its regular strip. Formula (6) equals the
summand of (3) at every retained physical index.

The [global numerator chart](research_mixed_fourier_right_cap_joint_global_chart.md)
proves \(\Pi_N\) holomorphic on \(\Re q>-1/N\) and
\(E_N\) holomorphic on \(\Re q<1\). Thus (6) is
holomorphic on the whole closed rectangle with real sides
\(\ell_N,b_N\) and any fixed finite heights \(\pm H\).
The incoming numerator may cross real part one, but it has
zeros there, not poles. Its exact period identity is
\[
 \Pi_N(q+1)=(1-e^{-2\pi iNq})\Pi_N(q).
\tag{7}
\]
Both terms of this multiplier remain in the following upper rate:
\[
 \mathfrak p(q)=
 \begin{cases}
 \Re g(q),&0<\Re q\le1,\\
 \Re g(q-1)+2\pi(\Im q)_+,&1\le\Re q\le6/5,
 \end{cases}
\]
\[
 \widehat R(t,\sigma)=\mathfrak p(a+t+i\sigma)
 +\Re\{g(b+t+i\sigma)-3g(t+i\sigma)-g(a)-g(b)
                                      +2\pi ia(t+i\sigma)\}.
\tag{8}
\]
The boundary values in (8) agree continuously. The original regular
factorial expansion on arbitrary compact strips, together with the
midpoint and reciprocal-midpoint bounds in
[uniform factorial estimates](research_uniform_factorial_and_boundary_decay.md),
gives, for every fixed \(H<\infty\),
\[
 |T_N(t+i\sigma)|\le C_{\tau,H}N^{A_{\tau,H}}
            e^{N(\widehat R(t,\sigma)+\tau)},\qquad
 \ell_N\le t\le b_N,\quad |\sigma|\le H .
\tag{9}
\]
This is the same zero-safe proof as Section 2 of
[nonnegative-height continuation](research_mixed_conditional_nonnegative_height_complete_source.md).
In particular, approaching the wall from the left uses
\(G_N(Nq)=N/G_N(N(1-q)-1)\); from the right it uses (7).
The midpoint shifts cost \(O(\log N)\). Both estimates include
their reciprocal zeros. There is no division by a period factor.

The exact split cotangent identity is
\[
 \sum_{j=L_N}^{M_N-1}T_N(j/N)
 =N\int_{\ell_N}^{b_N}T_N(t)\,dt+\mathcal R_N,
\]
\[
 \mathcal R_N=\frac{N}{2i}
 \left\{\int_{\partial R_H^+}T_N(s)[\cot(\pi Ns)+i]\,ds+
        \int_{\partial R_H^-}T_N(s)[\cot(\pi Ns)-i]\,ds\right\}.
\tag{10}
\]
Each sign-half boundary omits its real segment and has its original
induced orientation. These are exactly four vertical half-sides and
two horizontal sides. The constant-mode measure is \(+N\,dt\).

## 3. All six weighted currents

We recheck why the slope bounds from
[the lower-output source reduction](research_mixed_conditional_lower_output_middle_reduction.md)
hold on the deeper actual incoming range and at every fixed finite
height. Write \(A(q)=\Arg(1-e^{-2\pi iq})\) on the original
strip, and put \(\eta=-c\). Before the wall,
\[
 \partial_\sigma\widehat R
 =-A(a+s)-A(b+s)+3A(s)-2\pi x.
\tag{11}
\]
For \(\sigma\ge0\), its original argument bounds give
\[
 \partial_\sigma\widehat R
 \le2\pi-4\pi t+\max\{2\pi(z+t)-\pi,0\}\le9\pi/5.
\]
For \(\sigma\le0\), the outgoing radius is at most one;
its possible positive argument is at most
\(\pi/2-\pi(z+t)<\pi/4\). The incoming argument is
nonpositive and the own argument nonnegative. Hence
\[
                  \partial_\sigma\widehat R\ge-33\pi/20 .
\tag{12}
\]
These bounds use only the sign of \(\eta\), not its old upper bound.

After the wall put \(r_0=x+t-1\in[0,1/5]\). The derivative is
\[
 -A(r_0+i(\sigma-\eta))-A(b+s)+3A(s)-2\pi x
                              +2\pi{\bf1}_{\{\sigma>\eta\}}.
\tag{13}
\]
Here \(z+t>1/2\). For \(0\le\sigma\le\eta\) it is
at most \(\pi(2+2z-4t-2x)\le3\pi/10\); for
\(\sigma\ge\eta\) it is at most
\(\pi(5/2-x-3t+2z)\le9\pi/5\).
For \(\sigma\le0\), the incoming radius is at most one and its
argument at most \(\pi/2-\pi r_0\); the other two indicated
argument contributions are nonnegative. The derivative is therefore
at least \(-19\pi/10\). Thus globally,
\[
 \partial_\sigma\widehat R\le9\pi/5\quad(\sigma\ge0),
 \qquad
 \partial_\sigma\widehat R\ge-19\pi/10\quad(\sigma\le0).
\tag{14}
\]
Integrate the one-sided bounds at the finite kink in (8).

The half-grid cotangent remainders are bounded by
\(2e^{-2\pi N|\sigma|}\) on the verticals; the horizontals
have the same bound with constant four. Equations (14) pay all
verticals by their own real-cut rates. Their loss away from the
real axis is at least \(\pi|\sigma|/10\).
The [complete physical-row theorem](research_mixed_initial44_lower_right_physical_rows.md)
pays the products of both real cuts with the whole cap and the exact
Fourier allocations. It follows that all four complete weighted
verticals have the bound in (4), after the usual small cut allowance.

For the horizontal sides there is no need to impose a new numerical
action comparison. Let \(B_*\) be the fixed cap half-face plane
in the [action-calibration theorem](research_mixed_initial44_lower_right_action_calibration.md).
The complete cap times its first weight has upper rate \(B_*\).
On the compact actual parameter family and
\(3/40\le t\le1/2\), the continuous real rate
\(\widehat R(t,0)\) is bounded. Consequently the number
\[
 C_*=\sup\left\{
 B_*+\widehat R(t,0)-\tfrac12\Re g(b)
 -\Lambda(z)+\kappa_R(z-b_0)^2+2\delta_R\right\}
\tag{15}
\]
is finite. This supremum is only an existence definition; no value
is evaluated or assumed. All functions in it are the already fixed
continuous original phase or profile functions on compact source
domains. Choose one \(H>2\) with \(\pi H/10>C_*+1\).
By (14), each horizontal alias then has rate below
\[
                    \Lambda(z)-\kappa_R(z-b_0)^2-2\delta_R-1.
\tag{16}
\]
This height is fixed before \(N\); constants in (9) may depend on it.
The arbitrary finite-height domain proved in Section 2 is why this
choice is legitimate. No asymptotic limit of the contours as \(N\)
changes is taken.

## 4. The whole critical-height horizontal

The adopted action-calibration theorem supplies the same simple,
zero-lift critical point \(s_*=u_*+ih_*\), with
\[
 2/25<u_*<1-x,\qquad
 1/5<|e^{2\pi is_*}|<2,\qquad
 |h_*|<\log5/(2\pi).
\tag{17}
\]
The original phase
\[
 Q(s)=g(a+s)+g(b+s)-3g(s)-g(a)-g(b)+2\pi ias
\]
has \(\Re Q_{ss}<0\) throughout the strict prewall strip of
these heights. Thus its horizontal profile has its unique prewall
maximum at \(s_*\). We must also bound the postwall part.

Put \(U=e^{2\pi h_*}>1/2\), \(T=e^{-2\pi c}<5/3\),
and \(R=|Y|\le1\). The exact horizontal force of either
upper-rate branch is
\[
 e^{2\partial_t\widehat R(t,h_*)}
 =
 \frac{|T-Ue^{-2\pi i(x+t)}|^2
       |1-RUe^{-2\pi i(z+t)}|^2}
      {|1-Ue^{-2\pi it}|^6}.
\tag{18}
\]
The extra period rate in (8) is independent of \(t\).
On the postwall interval \(1-x\le t\le1/2\), one has
\(3/10\le t\le1/2\), \(1\le x+t\le6/5\).

If \(U\ge1\), use
\(\cos2\pi(x+t)>3/10\), \(\cos2\pi t<-3/10\),
and \(T\ge1\). Equation (18) is bounded by
\[
 \frac{(U^2-3U/5+25/9)(1+U)^2}
      {(U^2+3U/5+1)^3}<1.
\tag{19}
\]
The denominator minus numerator is
\[
 U^6+\frac95U^5+\frac{77}{25}U^4+\frac{302}{125}U^3
       +\frac{338}{225}U^2-\frac{142}{45}U-\frac{16}{9}.
\]
For \(U\ge1\), its fourth, third and second degree terms alone
exceed \(6U\); the remaining two high terms are positive.
The difference is therefore greater than
\(6U-142U/45-16/9\ge16/15>0\).

Now let \(1/2\le U\le1\). If \(3/10\le t\le7/20\),
then \(1\le x+t\le21/20\), so its cosine exceeds \(19/20\).
Convexity in \(T\in[1,5/3]\) gives the larger endpoint at
\(T=5/3\): the difference of the two endpoint bounds is
\(16/9-19U/15>0\). Hence (18) is at most
\[
 \frac{(U^2-19U/6+25/9)(1+U)^2}
      {(U^2+3U/5+1)^3}<1.
\tag{20}
\]
The exact difference is
\[
 P_1(U)=U^6+\frac95U^5+\frac{77}{25}U^4+
       \frac{3737}{750}U^3+\frac{1493}{225}U^2
                         -\frac{53}{90}U-\frac{16}{9}.
\]
It increases on \(U\ge1/2\), since already the derivative of
its quadratic and linear terms is positive there. At \(1/2\),
the quadratic, linear and constant terms sum to \(-31/75\);
the cubic term is \(3737/6000\), whose difference from
\(31/75\) is \(1257/6000>0\). The remaining terms are positive.

If \(7/20\le t\le1/2\), use instead
\(\cos2\pi t<-7/12\), keeping the incoming lower cosine
\(3/10\). Then (18) is at most
\[
 \frac{(U^2-3U/5+25/9)(1+U)^2}
      {(U^2+7U/6+1)^3}<1.
\tag{21}
\]
Its exact difference is
\[
 P_2(U)=U^6+\frac72U^5+\frac{73}{12}U^4
       +\frac{7763}{1080}U^3+\frac{811}{180}U^2
                          -\frac{131}{90}U-\frac{16}{9}.
\]
The derivative of its quadratic and linear terms is positive for
\(U\ge1/2\); every higher derivative term is positive. Direct
rational substitution gives \(P_2(1/2)=53/2160>0\).
All angle witnesses here follow from
\(\cos(\pi/10)>19/20\),
\(\cos(2\pi/5)>3/10\), and
\(\sin(\pi/5)>7/12\), using the elementary bounds already
proved in the physical-row theorem and the right-half theorem.

Equations (19)--(21) prove strict postwall descent at every possible
critical height in (17). The prewall and postwall statements join
continuously, including numerator zeros and both period alternatives.
Therefore the complete horizontal from \(\ell_N+ih_*\) to
\(b_N+ih_*\) has upper rate
\[
                       \Re\Theta(a,b)+\tau
\tag{22}
\]
for all large \(N\), with any prescribed cut allowance. Compactness
and the strict margins in (17) handle the small lower-cut displacement.
Multiplication by the whole cap and exact weights is paid by the
action-calibration theorem:
\[
 B_*+\Re\Theta(a,b)-\tfrac12\Re g(b)
 \le\Lambda(z)-\kappa_R(z-b_0)^2
                       -(\kappa+\kappa_R)(1/2-a_0)^2.
\tag{23}
\]
The last loss is strictly larger than \(\delta_R\).

## 5. The two unweighted sides and finite conclusion

Exact holomorphy gives
\[
\begin{split}
 \int_{\ell_N}^{b_N}T_N(s)\,ds
 ={}&\int_{\ell_N}^{\ell_N+ih_*}T_N(s)\,ds+
 \int_{\ell_N+ih_*}^{b_N+ih_*}T_N(s)\,ds\\
 &+\int_{b_N+ih_*}^{b_N}T_N(s)\,ds .
\end{split}
\tag{24}
\]
The positive \(N\) multiplier from (10) remains on all three terms.

On the left side, the prewall inequality \(\Re Q_{ss}<0\)
makes its real rate convex in height. It is bounded by its real
endpoint or its critical-height endpoint. The former is a complete
physical cut from Section 3; the latter is bounded by (22).
On the limiting right side \(t=1/2\), the exact argument bounds
of the lower-output Gaussian deformation give
\[
 \partial_\sigma\widehat R(1/2,\sigma)
 \le-2\pi(x-z)\le-\pi/10\quad(\sigma<\eta),\qquad
 \partial_\sigma\widehat R(1/2,\sigma)\ge0\quad(\sigma>\eta).
\tag{25}
\]
For the first inequality the period-shifted incoming argument is
nonnegative, the own argument is zero, and the outgoing argument is
at least \(-2\pi z\). For the second, the incoming argument is
at most \(\pi-2\pi(x-1/2)\), the outgoing argument is
nonpositive, and the second period branch supplies \(2\pi\).
These statements use only the signs of the external heights.
Thus the rate on the segment joining heights zero and \(h_*\)
is bounded by its larger endpoint. Uniform continuity of (8)
transfers this bound to the actual parity-dependent half cut \(b_N\),
including its possible kink. Its two endpoints are again paid by
Sections 3 and 4. No unweighted side is omitted.

Add the physical low and high blocks, (10), and (24).
Sections 3--5 pay all pieces of the literal finite source. The
number of rows, fixed contour lengths, exact residue densities and
their uniform symbols cost only polynomial factors or a prescribed
total rate allowance. The original first weight has upper rate zero
on (1), but both its factorial and forcing alternatives were retained
in obtaining that maximum. The outgoing halfweight remains
\(-\Re g(b)/2\) throughout; it is never canceled or divided out.
This proves (4).

The incoming ordinary color occurs only in the original cap, where
the full all-real estimate was used before multiplication. Its degree
is less than \(N\), so the original polynomial continuation theorem
gives fixed ordinary-color disks at arbitrary additional allowance,
then Cauchy gives fixed derivatives on smaller disks. This is not an
assertion of transverse derivatives of a nonholomorphic halfweight.
The original outside scalar and \(N\,da\) measure are unchanged.

The conclusion joins the complete unselected pair bound through
one half to the interval ending at \(7/10+ic\). A vertical reset at
that point, the subsequent real interval, a selected first path and
a whole first-period or whole-word estimate remain separate.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_initial44_right_half_interval.md | 309d6869f7438a9ed0a407c43666198ce1a039db7545c404a5e97f4ba2538c9c |
| research_mixed_initial44_lower_right_action_calibration.md | ef0079ed2c3148db13a24c23e715d9daab6e164b1aff0231de11041613e0106f |
| research_mixed_initial44_lower_right_physical_rows.md | 6665075b979801c0d5b9296738508be527bddd8827e3aea004b9ff1e7a60f702 |
| research_mixed_conditional_lower_output_middle_reduction.md | 9df0e7cdf4a193783e236e8e0fa8f416b5a123d8afe02033601be333cf6d5bc7 |
| research_mixed_conditional_lower_output_gaussian_deformation.md | 41c5d0030a8c057c1858e3e89e66136359aa3a448f881aeea93d23cf70a48fe8 |
| research_mixed_conditional_nonnegative_height_complete_source.md | 996b79b8427776f6789e0c2c4dda99ee83389833e53f7538330857468d2f3545 |
| research_mixed_fourier_right_cap_joint_global_chart.md | bf0069e52715e82c34be008c5814373017b43c019dd2a1a71dcd381e96b4da9f |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_uniform_factorial_and_boundary_decay.md | 4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11 |
| research_mixed_first_four_cap_lower_right_horizontal.md | 4d41a967edabf0710fc7b04b723bb3e2fb7a407d44bb5a0fc1678e3f9ee5ee6e |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |

No mathematical numerical evaluation, saved-value arithmetic, import,
test, compilation or frozen-source edit was performed.

