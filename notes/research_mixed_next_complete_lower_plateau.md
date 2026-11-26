# The full next source on its lower central interval

Research proof, 8 November 2026. The first incoming integration can
now be kept complete while the second incoming coordinate ranges over
the whole lower interval \(P+i\Im y_*\), \(P=[.22,.45]\).
The resulting source has a strict bound away from the geometric
coordinate and a nonzero asymptotic after integration over this
interval. This removes the restriction to the smaller following-image
corridor in the earlier lower-source theorem.

The statement concerns an ordinary third vertex after the prefix
\((3,4)\). The lower contour outside \(P+i\Im y_*\) and the
remaining part of the selected Fourier coefficient are not estimated.
No numerical evaluation or change to a frozen proof is used.

## 1. Exact source and actual references

Use the canonical ordinary-next family of
[the initial-interval theorem](research_mixed_next_unselected_incoming_initial_interval.md).
The flags are \((0,1,\beta)\), \(\beta=0,1\), and
\[
 (a_*,s_*,y_*,t_*,z_*)=(r_1,s_2^*,r_2,s_3^*,r_3),\qquad
 A=\Re a_*,\quad \alpha=\Re y_*,\quad
 h_a=\Im a_*,\quad h_y=\Im y_* .
 \tag{1}
\]
In particular \(h_a<0\), \(-.102<h_y<-.001\), and
\(A,\alpha\) lie strictly inside \(P\). All references retain
their original correlations and last typed input
\(s_4^*\in K_3\cup K_4\). Both vertices after the first cap
are ordinary.

For \(r=e^{-2\pi i/N}\), write \(P_j=(r;r)_j\) and
\(p_j(X)=(rX;r)_j\). The complete prefix and next kernel are
\[
\begin{split}
 F_N(w,Y)&=N\operatorname{CT}_X
       [U_{0,N}(w,X)C_{1,N}(X,Y)],\\
 U_{0,N}(w,X)&=\sum_{k<N}H_N(w,r^{-k})p_k(X)/P_k,\\
 C_{1,N}(X,Y)&=\sum_{j<N}X^{-j}p_j(X)p_j(Y)/P_j^3,\\
 C_{\beta,N}(Y,Z)&=\sum_{j<N}Y^{-j}p_j(Y)p_j(Z)/P_j^{2+\beta}.
\end{split}
\tag{2}
\]
Keep the original degree-at-most-\(N-1\) Fourier polynomial
\(d_N\), characterized by \(d_N(r^b)=P_b^{-1}\).
Set
\[
 y=q+ih_y,\qquad z=u+i\Im z_*,\qquad q,u\in P,\qquad
 Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz}.
 \tag{3}
\]
The lower density, including the literal first integration, is
\[
 \mathscr D_{0,N}(w;y,z)=F_N(w,Y)d_N(Y)C_{\beta,N}(Y,Z).
 \tag{4}
\]
The full next transfer also contains its second Fourier coefficient:
\[
 \mathcal T_\beta[F_N]
   =N[Y^0](F_Nd_NC_{\beta,N})
       +N[Y^N](F_Nd_NC_{\beta,N}).
 \tag{5}
\]
Nothing in this note deletes the second term of (5).

Let \(\Lambda_{123}(z)\) be the original affine action plane
in [the left-taper theorem, equations (5)--(7)](research_mixed_next_unselected_incoming_left_taper.md).
At the actual output,
\[
 \Lambda_{123}(z_*)=
 \Re\mathcal P_\beta^+(-2,z_*)-\frac{\beta}{2}\Re g(z_*),
 \qquad \kappa=1/2500000.
 \tag{6}
\]
The holomorphic action \(\mathcal P_\beta^+\) is the unchanged
next-source action from
[the local contribution theorem](research_mixed_three_four_next_local_source.md).
All primitives and their logarithmic lifts have the same
absolute normalization.

## 2. A complete first-contour bound

For the first integration use the fixed increasing-coordinate cycle
\[
\begin{split}
 \Gamma_a={}&[0,.1]\ \cup\
 \{x+ih_a(x-.1)/.12:.1\le x\le.22\}\\
 &{}\cup [\, .22+ih_a,.45+ih_a\,]\ \cup\
 [\, .45+ih_a,.5+ih_a\,]\\
 &{}\cup[\, .5+ih_a,.5\,]\ \cup[\, .5,1\,].
\end{split}
\tag{7}
\]
The endpoints are identified in the logarithmic cylinder.
The finite integrand in (2) is holomorphic in \(X\ne0\);
all these deformations stay in that punctured plane.
Consequently
\[
 F_N(w,Y)=N\int_{\Gamma_a}
       U_{0,N}(w,e^{-2\pi ia})C_{1,N}(e^{-2\pi ia},Y)\,da
 \tag{8}
\]
is an exact identity, with the original orientation and factor \(N\).

Write \(F_N=F_N^{\mathrm{cent}}+R_N^a\), where the central
term is precisely the integral in (8) over \(P+ih_a\).
Here \(R_N^a\) denotes this contour remainder only; it is
not the older physical-node deletion with a similar label.
The initial-interval, left-taper, and
[right-tail](research_mixed_next_unselected_incoming_right_tail.md)
theorems give
\[
 |R_N^a(w,Y)d_N(Y)C_{\beta,N}(Y,Z)|\,|d_N(Z)|^{\beta/2}
 \le C N^B e^{N(\Lambda_{123}(z)-10^{-11})}
 \tag{9}
\]
uniformly on (1)--(3) and for all real ordinary colors.
The corner inside the right tail is used as its combined
oriented integral. No separate absolute estimate of its
original horizontal and vertical pieces is assumed.
The other factors are independent of \(a\), so the
right-tail integral estimate applies directly to (9).

For the central term use the complete cap plane and the two
ordinary conditional planes from
[the retained-prefix interior theorem, Sections 2--3](research_mixed_retained_prefix_unselected_plateau.md).
They are valid for the full independent targets
\((x,q,u)\in P^3\), at their actual reference heights.
Each internal variable belongs to two planes.
Their incoming linear terms cancel at the original stationary
point, and their remaining outgoing linear term is exactly (6).
For every prescribed \(\tau>0\),
\[
\begin{split}
 &|U_{0,N}(w,e^{-2\pi i(x+ih_a)})
        C_{1,N}(e^{-2\pi i(x+ih_a)},Y)
        d_N(Y)C_{\beta,N}(Y,Z)|\,|d_N(Z)|^{\beta/2}\\
 &\quad\le C_\tau N^{B_\tau}
  \exp N\{\Lambda_{123}(z)
       -2\kappa(x-A)^2-2\kappa(q-\alpha)^2+\tau\}.
\end{split}
\tag{10}
\]
The unused outgoing quadratic loss has been dropped. The
two incident halfweights at \(Y\) give exactly \(d_N(Y)\);
the first coordinate has no Fourier weight because its flag
is zero. These allocations explain both the coefficient
\(2\kappa\) and the single outside halfweight in (10).
Every finite conditional row and every cap contribution is
already included in those complete-source planes.

Integrating (10) in \(x\), adding (9), and absorbing the
finite number of terms proves:

**Theorem 1.** For every \(\tau>0\), uniformly on (1)--(3),
at both level parities and for every real \(w\in[-2,2]\),
\[
\boxed{\quad
 |\mathscr D_{0,N}(w;y,z)|\,|d_N(Z)|^{\beta/2}
 \le C_\tau N^{B_\tau}
 \exp N\{\Lambda_{123}(z)
       -\min(2\kappa(q-\alpha)^2,10^{-11})+\tau\}.
\quad}
\tag{11}
\]
This is a bound on the complete \(F_N\), not merely on its
central first-contour portion. It does not assert that
\(F_N\) has a moving critical-point expansion at every \(q\).

The estimates persist on sufficiently small fixed outside
parameter neighborhoods when a positive gap is specified.
For weighted products one uses their integer-power holomorphic
squares before taking Cauchy bounds, as in the ordinary source
theorem. Only the known nonzero outgoing packet at \(z_*\)
is removed. Fixed real-color derivatives have polynomial cost.

## 3. The complete lower central integral has a nonzero coefficient

Define
\[
 \gamma_0=P+ih_y,\qquad
 I_{0,N}(w,z)=N\int_{\gamma_0}\mathscr D_{0,N}(w;y,z)\,dy.
 \tag{12}
\]
All contours in (7),(12) stay fixed at their base reference.
By (9), the difference between (12) and the exact two-variable
interior integral
\[
\begin{split}
 I_N^{\mathrm{int}}(w,z)
  =N^2\int_{P^2}
  &U_{0,N}(w,e^{-2\pi i(x+ih_a)})
   C_{1,N}(e^{-2\pi i(x+ih_a)},e^{-2\pi i(q+ih_y)})\\
  &{}\cdot d_N(e^{-2\pi i(q+ih_y)})
   C_{\beta,N}(e^{-2\pi i(q+ih_y)},e^{-2\pi iz})\,dx\,dq
\end{split}
\tag{13}
\]
is exponentially smaller than the original next action on
fixed small complete-color/output neighborhoods. The outgoing
halfweight is removed using its original nonzero packet there.
Equation (13) is the integral of the retained-prefix theorem
for the flags \((0,1,\beta)\), with no terminal Gram factor.

**Theorem 2.** On those neighborhoods, uniformly over the
compact ordinary-next families and at both level parities,
\[
 \boxed{\quad
 I_{0,N}(w,z)=N^{-2-\beta/2}\mathcal A_\beta(w,z)
       e^{N\mathcal P_\beta^+(w,z)}
                   (1+O_{\rm hol}(N^{-1})),\qquad
                    \mathcal A_\beta\ne0.
 \quad}
 \tag{14}
\]
Every fixed derivative of the relative error is \(O(N^{-1})\)
on smaller neighborhoods. The coefficient is the original
Gaussian coefficient, not a newly selected normalization.

Indeed the retained-prefix theorem gives (14) for (13).
Its general power \(N^{-1-k+\epsilon_m/2}\) becomes
\(N^{-2-\beta/2}\), since \(k=1+\beta\) and
\(\epsilon_m=\beta\). The error (9) is exponentially smaller
and hence remains within the stated relative error.
The local symbol and square root of the Gaussian determinant
are nonzero on the same branch as the local next-source theorem.

More explicitly, choose a fixed local segment
\(J_*\subset\gamma_0\) containing \(y_*\), with its endpoints
inside the original packet neighborhood, and choose \(\rho>0\)
such that
\[
 \{q+ih_y:|q-\alpha|<\rho\}\subset J_*.
\]
Put
\[
 \eta_\rho=\tfrac1{32}\min(2\kappa\rho^2,10^{-11})>0.
 \tag{15}
\]
Choose the rate tolerance and outside neighborhoods strictly
within this reserve. Theorem 1, integration, and Cauchy's
formula then give, for each fixed derivative order,
\[
 \partial^\nu\!\left[
 e^{-N\mathcal P_\beta^+(w,z)}
 N\int_{\gamma_0\setminus J_*}\mathscr D_{0,N}\,dy
 \right]=O_\nu(e^{-\eta_\rho N}).
 \tag{16}
\]
Thus the whole lower central integral differs from the original
local geometric integral \(I_{\mathrm{geom},N}\) by a controlled
exponentially small term. Unlike the previous following-image
corridor estimate, (16) covers all of
\(\gamma_0\setminus J_*\).

## 4. The same conclusion for the original filtered meromorphic kernel

For comparison with the remaining signed contour, retain exactly
the old cardinal filter of
[the filtered selected-plateau theorem](research_mixed_next_filtered_selected_plateau.md).
Write
\[
 F_N^{\rm mid}=(I-\Pi)(F_N-R_N^{\rm node}),\qquad
 E_N=F_N-F_N^{\rm mid},\qquad
 K_N(y)=\frac{N F_N^{\rm mid}(w,Y)d_N(Y)C_{\beta,N}(Y,Z)}
                   {1-Y^N}.
 \tag{17}
\]
The superscript in \(R_N^{\rm node}\) distinguishes the
original physical-node deletion from the contour remainder
in Section 2. The filter retains its original upper cutoff
\(11/12\) and original fixed lower cutoff.

The full correction polynomial has disk bound
\[
 \sup_{|Y|\le1}|E_N(w,Y)|\le C N^B e^{77N/50}.
 \tag{18}
\]
The actual unselected marginal argument in
[paired localization, Lemma 1](research_mixed_next_low_cardinal_paired_localization.md)
uses only this disk bound. Consequently (18), with the entire
remaining weight and third kernel, is below the same action
plane by a fixed gap greater than \(1/20\) on (3).
No physical-node range is replaced by an open contour arc.

On \(\gamma_0\),
\[
 |Y^N|=e^{2\pi Nh_y}\le e^{-\pi N/500},\qquad
 |1-Y^N|\ge\tfrac12
 \tag{19}
\]
for all sufficiently large levels. The exact difference is
\[
 K_N-N\mathscr D_{0,N}
 =N\left\{\frac{Y^NF_N-E_N}{1-Y^N}\right\}
                         d_N(Y)C_{\beta,N}(Y,Z).
 \tag{20}
\]
The first term uses Theorem 1 with its nonnegative loss
dropped and the strict penalty in (19); the second uses (18).
Both are exponentially smaller than the original next action,
uniformly over the whole lower central interval.
Their reserves are larger than (15).
It follows that
\[
 \partial^\nu\!\left[
 e^{-N\mathcal P_\beta^+(w,z)}
 \left\{\int_{\gamma_0}K_N(y)\,dy-I_{\mathrm{geom},N}\right\}
 \right]=O_\nu(e^{-\eta_\rho N}),
 \tag{21}
\]
after a harmless reduction of the outside neighborhoods.
This includes the exact denominator and the original \(N\).

## 5. What is left of the signed contour

Let \(s>0\), \(H=1/100\), and
\(\Gamma_0=[0,1]+ih_y\) be the unchanged choices in
[upper seam-arc removal](research_mixed_next_top_seam_arc_removal.md).
Its remaining signed expression was
\[
 \int_{\Gamma_0\setminus J_*}K_N\,dy
 -\int_{[s,.22]+iH}K_N\,dy
 -\int_{[.45,1-s]+iH}K_N\,dy .
\]
By (16)--(21), it may now be replaced, with a controlled
exponentially small error, by
\[
 \boxed{\quad
 \int_{\Gamma_0\setminus\gamma_0}K_N\,dy
 -\int_{[s,.22]+iH}K_N\,dy
 -\int_{[.45,1-s]+iH}K_N\,dy .
 \quad}
 \tag{22}
\]
The upper-minus signs are unchanged. There are no omitted
vertical sides: the older cyclic identity canceled them
exactly by period one.

Equation (22) is still an unestimated signed remainder.
The present theorem completes the lower central interval,
not either whole Fourier coefficient. The full third-tangle
asymptotic and stability under arbitrary short partial fillings
therefore remain open.
