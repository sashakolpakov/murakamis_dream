# A full first collar, independent plateau buffers, and arbitrary middle states

Research deduction, 6 November 2026. The complete first-collar prefix
bound supplies an active left boundary datum for the contracted
collar theorem. The second target ranges over its whole proved typed
interval, and all subsequent buffer targets range independently over
the plateau. No small coherent buffer neighborhood is required. The
middle retains every original hybrid state. The first-collar input
also extends to all real outside colors, by keeping its coherent
private-row coefficients and bounding its physical endpoint rows
separately.

This improves the target domain and real-color scope of
[the earlier full-collar buffered theorem](research_mixed_full_collar_buffered_sectors.md).
It is still a specified sector estimate, not whole-source dominance.
No new analytic or numerical evaluation is used.

## 1. The first seam ceilings hold over the whole real color period

Retain the exact cap identity from
[the seam-source theorem](research_mixed_cap_seam_source_bounds.md):
\[
 U_{\alpha,N}(w,1)=\sum_{i=0}^{N-1}
   D_N(i/N)^{-1}\mathcal C_N(i/N,w)P_i^{1-\alpha},
 \qquad |D_N(i/N)|=1,
\tag{1}
\]
where \(\alpha=0,1\), \(P_i=(r;r)_i\), and
\(r=e^{-2\pi i/N}\). Put \(S_i=|P_i|\).
For every compact physical-index interval inside \((0,1)\),
Theorem 1 of
[endpoint real-color decay](research_mixed_endpoint_real_color_decay.md)
gives, uniformly for real \(\theta\),
\[
 |\mathcal C_N(i/N,-2\cos\theta)|
   \le CN^A e^{N\lambda(i/N)},\qquad \lambda(s)=\Re S(s).
\tag{2}
\]
Its favorable angular loss has been discarded. Thus the compact
private-row rates in (1) remain
\(f_\alpha(s)=\lambda(s)+(1-\alpha)J(s)\).
The exact derivative identities and the already saved scalar
bounds of the seam-source theorem give their same ceilings
\[
                         b_0=101/125,\qquad b_1=433/500.
\tag{3}
\]

The physical index endpoints require a separate argument. Replace
the complete-color Newton values in that theorem by
\(E_l(\theta)=|e_l(-2\cos\theta)|\). The literal support
\(l\le i\) gives
\[
 |\mathcal C_N(i/N,-2\cos\theta)|
       \le\sum_{l=0}^{i}\frac{E_l(\theta)}{S_lS_{i-l}}.
\tag{4}
\]
For \(s=i/N\le1/100\), the exact numerator bound
\(E_l(\theta)\le4^l/S_l^2\) is uniform for
\(-2\cos\theta\in[-2,2]\). The same zero-safe product
estimate consequently has rate
\[
             2s\log2-4J(s)<1/4.
\tag{5}
\]
The factor \(P_i\) for \(\alpha=0\) only lowers this rate.

At the other endpoint put \(k=N-1-i\). The exact identity
\(S_{N-1-j}=N/S_j\), and
\(S_{k+l}/S_l\le2^k\), give
\[
 \begin{split}
 |\mathcal C_N(i/N,-2\cos\theta)|
       &\le\frac{2^k}{N}\sum_{l=0}^{i}E_l(\theta),\\
 |P_i\mathcal C_N(i/N,-2\cos\theta)|
       &\le\frac{2^k}{S_k}\sum_{l=0}^{i}E_l(\theta).
 \end{split}
\tag{6}
\]
The all-real-color zero-safe Newton estimate, recorded in equation
(5) of endpoint real-color decay, uses
\[
 V_\theta(x)\le V_0(x)\quad(0\le x\le1/2),\qquad
 V_\theta(x)\le0\quad(1/2\le x\le1).
\tag{7}
\]
The maximum of the lower-half \(V_0\) is less than \(3/5\).
Therefore \(\sum_l E_l(\theta)\le CN^A e^{3N/5}\),
uniformly in the color. For \(k/N\le1/100\), (6) has the same
rates below \(.61\) and \(.65\) as the original seam proof.
Both are below (3). In particular no inequality
\(V_\theta\le V_0\) is asserted on the upper Newton half.

Combining compact rows and endpoint rows proves, for every
prescribed \(\eta>0\),
\[
 \sum_{i<N}|\mathcal C_N(i/N,-2\cos\theta)|\,|P_i|^{1-\alpha}
       \le C_\eta N^{A_\eta}e^{N(b_\alpha+\eta)}
       \qquad(-\pi\le\theta\le\pi).
\tag{8}
\]
The inner endpoint coefficient has stayed whole in the compact
rows; only the justified endpoint rows use (4). This is not a
replacement of that coefficient by an absolute Newton sum near
its interior saddle.

The existing zero-safe collar transfer estimates only the factor
\(p_i(X)/P_i\), independently of the ordinary color. Thus, for
the same fixed sufficiently small \(\rho>0\), (8) gives
\[
 |U_{\alpha,N}(-2\cos\theta,e^{-2\pi ix})|
 \le C_\eta N^{A_\eta}
          e^{N(b_\alpha+\Delta_\rho+\eta)},\qquad
 0\le x\le\rho,\quad
 \Delta_\rho=\rho\log2-J(\rho).
\tag{9}
\]
Every first diagonal and selected monomial is still allocated
separately. The latter has modulus one on this real collar.
The same conclusions hold at both parities. Fixed ordinary-color
jets follow with polynomial cost from the separate degree bound
\(\deg_w U<N\), using the inverse-angle estimate on color
circles of radius \(N^{-2}\), as in the endpoint real-color
theorem. No angular loss is claimed for (8) or (9).

## 2. The complete prefix, with its original cut marginal

Let the first two types be \((3+\alpha,3+\beta)\).
Use
\[
 z_1=x_1\in[0,\rho],\qquad
 z_2=y_2+ik,\qquad
 y_2\in I_{3+\beta},\quad
 I_3=[.267,.433],\quad I_4=[.24,.363].
\tag{10}
\]
Keep \(\sigma_1\in\{0,\alpha\}\). When \(\beta=0\),
coordinate two is unselected and \(k\) lies between its actual
height \(c_2\) and zero. When \(\beta=1\), permit either
\(\sigma_2=0,\ c_2\le k\le0\), or
\(\sigma_2=1,\ 0\le k\le7/500\). All later coordinates
of this prefix are unselected at their original heights and range
independently over \(P\).

The complete first-collar result required here is the ordinary-cut
prefix theorem, equation (11) of
[three-row source assembly](research_mixed_three_row_source_assembly.md),
also used in Section 4 of
[first-collar terminal completion](research_mixed_first_collar_full_terminal_completion.md).
For a cut \(\ell\ge3\), its literal product is
\[
 \mathcal L_{\ell,N}=
 \left|U_{\alpha,N}(w_L,X_1)\prod_{j=2}^{\ell}C_{\epsilon_j,N}\right|
       \prod_{j=1}^{\ell-1}|D_j|\ |D_\ell|^{1/2}.
\tag{11}
\]
Only the first two retained selections may be nonzero. It obeys
\[
 \begin{split}
 N^{-1}\log\mathcal L_{\ell,N}
 \le{}&M_\ell+\Re P_{\ell,b}(y_\ell-a_\ell)
                   -\delta_{\alpha\beta}+\eta\\
 &-\kappa_*\left\{(y_2-a_2)^2+
           2\sum_{j=3}^{\ell-1}(y_j-a_j)^2+
                           (y_\ell-a_\ell)^2\right\}
       +O_{\eta,m}(\log N/N),\\
 \kappa_*={}&1/2500000,\qquad
 (\delta_{00},\delta_{10},\delta_{01},\delta_{11})
              =(3/100,3/125,4/125,4/125).
 \end{split}
\tag{12}
\]
The action and cut marginal are those of this prefix in the
original full-word reference. The cut is not declared a new
closed endpoint or a new critical word.

All source ingredients of (12) except the first cap are color
independent. Its first-pair upper uses precisely the ceiling
\(b_\alpha+\Delta_\rho\), now available in (9) for every real
color. The phase floor and tangent are still calibrated at the
unchanged complete-color reference. Therefore the original proof
of (12) applies over the full real left-color period as well.
For second type four it pays the fixed \(9/500\) allowance once
on edge three, from the first-pair reserve \(1/20\). For second
type three its height allowance was already paid in the first
pair. No height charge is repeated on later edges.

The existing small complex color disks and all fixed color jets
are retained. Only coordinate two has a changed height beyond
the real first collar. Its real target interval lies in \(P\),
so the cutoff acting on coordinate three is one. All subsequent
prefix heights stay at their original values.

## 3. An active first collar with arbitrary middle states

Use the exact contracted chart, safe interval, two 711-symbol good
blocks, and arbitrary intervening interval \(J\) of
[contracted boundary collars](research_mixed_contracted_boundary_collar_completion.md).
Replace only its left physical condition by (10) and its two
selection choices. All positions from three to \(J\), including
the left good block, range independently over \(P\) and are
unselected. The right physical region is independently unselected
plateau, except for the optional completed last selection
\(\tau\) under the same suffix hypotheses as that theorem.
Every original hybrid state remains permitted in \(J\).

Take \(\ell=p-1\) in (12), where \(p\) is the ordinary
middle cut. This is exactly the literal left boundary modulus
of that theorem. Its cut coordinate has its original height, so
the horizontal marginal in (12) equals the original complex
affine marginal on that displacement. Original stationarity gives
\(P_{p-1,b}+P_{p,a}=0\). Thus the same source and six-edge
closure yield the improved left inequality
\[
 B_{L,N}-D_L
 \le-\delta_{\alpha\beta}
         -\tfrac1{10}(u_L-a_{u_L})^2+\mathfrak e_{L,N}.
\tag{13}
\]
The \(1/10\) term is supplied by the exact coherent edge at
\(j=g_L+2\), not by increasing \(\kappa_*\) in (12).
All first-collar allowances have already been included in
\(\delta_{\alpha\beta}\). The actual first cap is not
replaced by a supporting plane outside its original domain.

The right inequality, both relative pinning replacements and both
inner occupation fees are unchanged. Consequently
\[
 \begin{split}
 N^{-1}\log|\mathscr J_{\sigma,N}|-M_{\rm open}
 \le{}&-\delta_{\alpha\beta}-\tau\delta_T
        -\frac1{40000}\sum_{j\in M}p_j^{\rm pin}\\
 &-\frac1{20}\{(u_L-a_{u_L})^2+(v_R-a_{v_R})^2\}
        +\eta+C_{\eta,m}\log N/N,
 \qquad \delta_T=1/2600.
 \end{split}
\tag{14}
\]
One aggregate tolerance \(\eta\) covers all original finite
source factors. This holds on small complex color neighborhoods
and over both full real color periods. The middle loss and all
reset charges inside its original hybrid weights remain present.

Since every \(\delta_{\alpha\beta}\ge3/125\), choose
\(\eta<1/250\). Summing all permitted first, second and middle
selections, integrating this fixed sector, and restoring the
original scalar gives the common finite gap
\[
                         1/50+\tau/5200.
\tag{15}
\]
The graph Jacobian and all original powers of \(N\) affect only
the polynomial prefactor. Both level parities and fixed color jets
are included. No nonplateau middle symbol is required: the active
first collar already provides a strict reserve.

## 4. Partial-source consequence and the remaining boundary states

The new region has \(x_1\in[0,\rho]\), disjoint from every
plateau sector and from the sectors of the contracted-collar theorem,
whose first coordinate lies in \(P\). Fix the collar positions
and count each permitted Fourier sector once. Adding these new
integrals to any of those specified disjoint partial sums retains
separate ordinary degree at most \(N-1\). Their uniform exponential
loss (15) preserves the original nonzero \(N^{-3/2}\) packet
on smaller complex color neighborhoods, and changes its real
outside-color gap only by taking the minimum with the new gap.
The same degree/local-packet stability lemma then supplies its
quadratic complex strip estimate. No cancellation or positivity of
source coefficients is assumed in this conclusion.

Compared with the 5 November full-collar buffered theorem, the
second real target now occupies all of \(I_{3+\beta}\), every
later physical buffer coordinate occupies independent \(P\),
the terminal source is fully contracted before taking moduli, and
the bound covers the entire real outside-color square. The two
long unselected corridors are still required. This does not control
second targets outside \(I_{3+\beta}\), a bad state entering a
required corridor or another uncontrolled physical boundary state,
short words without the blocks, or the whole original source.
