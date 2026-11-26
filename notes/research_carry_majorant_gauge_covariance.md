# Gauge covariance of the actual carry-current majorant

Private written proof, 19 November 2026.

Tensor dilations do not move the same source point into the sharper
carry-current domain. When the crossing matrices, current, coherent
coordinates and closing adapter are transformed together, the proved
positive majorant has exactly the same exponential base. Unequal
endpoint frames require a transformed identity kernel as well.

This identifies a restriction on using the composition theorem W at a
geometric point. It is not an exclusion of other polarizations or of
stronger estimates obtained after genuine finite contractions.

## 1. Finite frames, kernels and the closing adapter

Use W's physical space \(V_N^{\otimes m}\), with \(m,N\ge2\),
\(d=N-1\), occupations \(0\le a_j\le d\), and its actual fixed-root
meridian family \(M=e^\mu\). For \(g\in(\mathbb C^*)^m\), write
\[
 G(g)e_{\mathbf a}=g^{\mathbf a}e_{\mathbf a},\qquad
 g^{\mathbf a}=\prod_jg_j^{a_j}.
 \tag{1}
\]
The frames may vary holomorphically with \(\mu\), provided their
entries remain nonzero on the domain in question. Let
\(A_c\cdots A_1=W_\beta\) be any actual mixed signed braid word,
with the common crossing scalar stripped as in W. The prescribed
crossing and framing scalar lines remain external and unchanged.
For frames \(G_0,\ldots,G_c\), set
\[
 A_\ell^g=G_\ell^{-1}A_\ell G_{\ell-1},\qquad
 W_\beta^g=G_c^{-1}W_\beta G_0.
 \tag{2}
\]
Every sum and every matrix here retains the original finite caps.

With W's input-binomial kernel, direct entry substitution gives
\[
 K_{G_c^{-1}AG_0}(z',w')
       =K_A(\widehat z,\widehat w),\qquad
 \widehat z_j=z'_j/g_{c,j},\quad
 \widehat w_j=g_{0,j}w'_j.
 \tag{3}
\]
In particular the identity between the two endpoint frames is
\[
 J_g=G_c^{-1}G_0,\qquad
 K_{J_g}(z',w')=
       \prod_j\left(1+\frac{g_{0,j}}{g_{c,j}}z'_jw'_j\right)^d
       =I_N(\widehat z,\widehat w).
 \tag{4}
\]
For unequal endpoints, replacing (4) by the bare identity kernel
changes the normalization. It is not the comparison in W.

For a diagonal closing coupon \(C(\mu)\), the exact source equality is
\[
 \operatorname{Tr}(CW_\beta)
  =\operatorname{Tr}(C^gW_\beta^g),\qquad
                  C^g=G_0^{-1}CG_c.
 \tag{5}
\]
This includes the prescribed physical highest-cut projector and
diagonal pivots, with any outside scalar line still multiplied in.
If \(G_c=G_0\), then \(C^g=C\). Otherwise the indicated boundary
adapter must remain. Equations (2)--(5) are whole-family identities.
Moving-frame connection terms cancel in the complete trace, not in
each local kernel or a restricted integration window. Differentiating
(3) with moving frames also differentiates its displayed coordinates.

## 2. The positive maps and their invariant products

W's root column majorants for the two crossing signs are
\[
 U_+(s_1,s_2)=(s_2+2s_1,s_1),\qquad
 U_-(s_1,s_2)=(s_2,s_1+2s_2).
 \tag{6}
\]
They act as the identity on spectator coordinates. Let \(U_\ell\)
be the corresponding map at stage \(\ell\), and let \(U_\beta\)
be their backwards composition, so the last output weight is
propagated first. Componentwise multiplication and division are used
in the next formulas.

More generally, for any actual finite matrix define its weighted
absolute column sum by
\[
 Z_A(s;\mathbf a)=\sum_{\mathbf b}|A_{\mathbf b,\mathbf a}|
                                                s^{\mathbf b}.
\]
The exact frame rule is
\[
 Z_{G_\ell^{-1}AG_{\ell-1}}(s;\mathbf a)
   =|g_{\ell-1}|^{\mathbf a}
                     Z_A(s/|g_\ell|;\mathbf a).
 \tag{7}
\]
Thus the majorant transported from (6) is precisely
\[
 U_\ell^g(s)=|g_{\ell-1}|\,
                         U_\ell(s/|g_\ell|),\qquad
 U_\beta^g(s)=|g_0|\,U_\beta(s/|g_c|).
 \tag{8}
\]
The second equality follows by cancelling each adjacent diagonal
factor in the backwards composition. It applies to every mixed
signed word; the maps in (6) need not be inverses. W's polynomial
meridian-collar losses are unchanged when transported by the exact
rule (7). No bound on the condition number of a frame is substituted.

Fix the current pair \(p,r=p+1\). Its degree projector commutes
with every \(G_0\). Transport the actual current as well:
\[
 C_{E,F}^g=G_0^{-1}C_{E,F}G_0,\qquad
 W_\beta^gC_{E,F}^g=G_c^{-1}W_\beta C_{E,F}G_0.
 \tag{9}
\]
Here \(C_E=E_{pr}\mathbf1_{J_{pr}=N}\) and
\(C_F=F_{pr}\mathbf1_{J_{pr}=d}\), where
\(J_{pr}=J_p+J_r\) is pair occupation,
\(E_{pr}=E_pK_r+E_r\), and \(F_{pr}=F_p+K_p^{-1}F_r\).
For example \(G_0^{-1}E_jG_0=g_{0,j}E_j\) and
\(G_0^{-1}F_jG_0=g_{0,j}^{-1}F_j\); these coefficients cannot
be omitted while claiming to transport the same current.

Put
\[
 X_j^g=U_{\beta,j}^g(|z'|)|w'_j|
      =U_{\beta,j}(|\widehat z|)|\widehat w_j|,
 \qquad v_j^g=\frac{g_{0,j}}{g_{c,j}}z'_jw'_j
                       =\widehat z_j\widehat w_j.
 \tag{10}
\]
The correctly normalized transported base is
\[
 \boxed{\quad
 \mathcal B_{\beta,p}^g(z',w')=
 \frac{(\sqrt{X_p^g}+\sqrt{X_r^g})^2
                   \prod_{j\ne p,r}(1+X_j^g)}
      {\prod_j|1+v_j^g|}
 =\mathcal B_{\beta,p}(\widehat z,\widehat w).
 \quad} \tag{11}
\]
Indeed (3),(4),(9) identify the entire normalized finite current
with the old one; (7),(8) identify its actual column estimate and
(10) each factor in W's divided-shell bound. This proves (11)
without multiplying coherent symbols.

At the same point written in the new coordinates,
\(z'=g_cz\), \(w'=g_0^{-1}w\), both \(X_j^g=X_j\) and
\(v_j^g=v_j\). In the cyclic case \(g_c=g_0\), the latter
are the ordinary products \(z'_jw'_j\). Thus tensor dilation
cannot change whether this point satisfies the proved criterion
\(\mathcal B_{\beta,p}<1\). Equation (7) also shows why an
entrywise absolute sum cannot improve merely by such a relabelling.

## 3. The coarser two-sided bound must retain its weights

The same argument applies to W's two-sided currents, including all
intervening carry projectors. Those projectors commute with the frames.
For an operator from the initial to the final frame, define the
transported column norm by
\[
 \|A^g\|_{g_c,g_0;1}
      :=\|G_cA^gG_0^{-1}\|_1.
 \tag{12}
\]
It is the operator norm for the corresponding weighted finite
\(\ell^1\) spaces. With this norm the original \(3^{cd}\)
column estimate, the threshold support, and every Vandermonde
step of W remain exactly the same. Hence the transported coarse
base is
\[
 \Omega_{m,c}(\widehat\tau),\qquad
 \widehat\tau=
    \max_j|z'_j/g_{c,j}|\,\max_j|g_{0,j}w'_j|,
 \quad
 \Omega_{m,c}(t)=3^c\frac{m^m}{(m-1)^{m-1}}
                         \frac{t}{(1-t)^m}.
 \tag{13}
\]
Its usual range is \(0\le\widehat\tau<1/(m-1)\).
At matched coordinates, \(\widehat\tau\) equals the original
\(\tau\). For a common cyclic dilation \(g_j=t_0\) on every
head, even the bare product of the two maxima is unchanged.

For unequal head dilations, the bare maxima in the new coordinates
can change. The new unweighted matrix column norms change too.
One cannot keep the old \(3^{cd}\) estimate and use only the more
favorable bare maxima. Formula (13) proves covariance of the
transported estimate, not invariance of every possible separately
optimized matrix-norm bound. Likewise an \(N\)-dependent or moving
frame does not provide new uniform compactness or derivative bounds;
those must be checked in its actual pulled-back coordinates.

## 4. The remaining geometric frame does not tune the criterion

G's complete critical-scheme theorem supplies a specific geometric
application, with its hypotheses retained. At a complete faithful
point with regular semisimple total product, its resolved reduction
sets \(F_\Sigma=0\) and removes the upper-unipotent framing motion.
The remaining continuous common frame is
\[
                         p_j\longmapsto\lambda p_j.
 \tag{14}
\]
In G's coordinates, (14) fixes \(K_j\) and sends
\(e_j\mapsto\lambda e_j\), \(f_j\mapsto\lambda^{-1}f_j\).
The two choices of the total eigenflag are discrete, not another
continuous gauge. With G's additionally supplied positive complete
gluing certificate, quotienting (14) leaves a reduced geometric point.

Suppose an actual physical-spin chart has been matched to this
correspondence. The common action (14) is the reciprocal dilation
\[
                 z_j\longmapsto\lambda^{-1}z_j,
                 \qquad w_j\longmapsto\lambda w_j.
 \tag{15}
\]
This sign can be checked without a semiclassical kernel theorem:
an \(E_j\) arrow has output degree one less than input, so its
kernel scales by \(\lambda\) under (15); an \(F_j\) arrow
scales by \(\lambda^{-1}\), and \(K_j\) has degree zero.
The same scaling holds for their normalized kernels. It is precisely
the action on the three coordinates in G.

Each literal crossing preserves global integer degree and therefore
commutes with the common tensor dilation. The diagonal closing coupon
does too. Moreover every map in (6) is homogeneous. Consequently
\(v_j\), \(X_j\), \(\mathcal B_{\beta,p}\), and \(\tau\)
are all unchanged under (15), with the word itself unchanged.
The residual continuous geometric frame thus cannot repair failure
of either proved inequality at the same matched point.

This conclusion uses G only at its stated complete root and on a
supplied matched spin chart. Its rational graph theorem does not
itself construct that analytic chart or identify a localized source
coefficient. Nor does the calculation compare the two discrete
eigenflag choices. It reduces the proposed diagonal-gauge shortcut
to an intrinsic test on each already matched branch.

General diagonal frames that are not exponential in occupation,
non-diagonal polarizations, Fourier adapters, changes of cut, and
different presentations are not excluded. Their actual kernels,
projectors and closing currents require their own estimates; they
cannot reuse (6) unchanged without a comparison. No geometric domain
coverage, original-cycle incidence, or closed-source lower bound is
inferred here.

## Complete proof directs

* W: `notes/research_actual_word_carry_current_composition.md` (496 lines),
  SHA256 `d7c9179a36ac9c9d96c3eb1f8db1e492e6b5a67b3ea56de34cffa57bc926a613`.
* G: `notes/research_actual_reduced_braid_critical_scheme.md` (564 lines),
  SHA256 `ddddcd9bf75f35afdf3e5de0c03323acee2c66e624db36142c2344ef729a977a`.

Both complete directs were freshly whole-read nontruncated in this
active author sequence. The new proof uses finite entry identities
and the stated geometric restriction only. No mathematical programs,
tests, builds, or edits to frozen or public files were used.
