# The actual reduced first jet in one hybrid spin polarization

Private written proof, 19 November 2026.

Both Cartan terms of the actual reduced pointed source have
one and the same finite spin-coherent integrand. Their
difference is carried by explicit rational scalar densities
at one interface. This remains exact with arbitrary cyclic
diagonal basis frames, including physical and factorial
choices on different heads. The whole meridian pole, its
specified integrated residue, and its first finite part are
retained.

The scalar first-normal density is a uniform unit on compact
complex charts whose total spin occupation is nonreal.
This supplies a source dual in the same polarization as
hybrid spin kernels. It does not estimate the angular
period or its geometric relative-cycle coefficient.

The finite spin resolution is existing coverage in
compact_coherent_source_period.md. The beta normalization
and rotation used here are proved directly. The complete
proof directs are R and G, pinned at the end.

## 1. Exact cyclic frames and the finite spin resolution

Fix \(N\ge3\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\),
\(m\ge2\), and \(r=m-1\). Put
\[
 x_0=-q^{-1},\qquad \varepsilon=(-1)^{(N+1)r},
 \qquad M=e^\mu .
 \tag{1}
\]
The quantum parameter is fixed when taking meridian
derivatives. Let \(W(M)\) be the actual braid family,
including its prescribed crossing and framing scalars,
and let
\[
 B(M)=\mathcal B_m(W(M))=A_L(M)\cdots A_1(M),
 \qquad L\ge1 .
 \tag{2}
\]
Use an identity factor for an empty word. R supplies the
actual reduced generators and the source functional.

Choose invertible diagonal frames \(D_\ell(M)\) on the
remaining tensor, with \(D_L=D_0\), analytic on the
meridian domain under discussion. They may depend on
\(N\). Set
\[
 T_\ell=D_\ell^{-1}A_\ell D_{\ell-1},
 \qquad
 T_L\cdots T_1=D_0^{-1}BD_0 .
 \tag{3}
\]
Tensor products of \(G_F\) and identity frames are
included. No condition-number estimate for these
frames is part of the present theorem.

For any finite matrix \(T\) on the \(r\) heads define
\[
 K_T(z,w)=\sum_{a,b\in\{0,\ldots,d\}^r}
                  z^a T_{ab}\binom db\,w^b ,
 \qquad \binom db=\prod_{j=1}^r\binom d{b_j}.
 \tag{4}
\]
On one complex coordinate use the probability measure
\[
 d\nu_N(u)=\frac N\pi(1+|u|^2)^{-N-1}\,d^2u .
 \tag{5}
\]
Angular integration and the beta integral give
\[
 \int u^a\bar u^{\,b}\,d\nu_N(u)
                  =\frac{\delta_{ab}}{\binom da}.
 \tag{6}
\]
For \(a=b\), the radial integral is
\(N\int_0^\infty v^a(1+v)^{-N-1}dv\).
Integration by parts \(a\) times, followed by the
elementary integral of \((1+v)^{-N-1+a}\), gives
\(a!(N-1-a)!/(N-1)!\), proving (6) for every
physical \(0\le a\le d\), including both endpoints.

Consequently the exact identity kernel is
\(\prod_j(1+z_jw_j)^d\), and (6) proves composition
and trace by multiplication of finite sums. In
particular define the one common closed integrand
\[
 \mathcal P_N(\mu;\mathbf u)=
 K_{T_L}(u_0,\bar u_{L-1})\cdots
 K_{T_1}(u_1,\bar u_0),\qquad
 d\boldsymbol\nu_N=\prod_{\ell=0}^{L-1}
                              \prod_{j=1}^r d\nu_N(u_{\ell,j}).
 \tag{7}
\]
For \(L=1\) use the single diagonal kernel. Then
\[
                  \int\mathcal P_N\,d\boldsymbol\nu_N
                                    =\operatorname{Tr}B .
 \tag{8}
\]
The domains can be regarded as compact products of
spheres. In the affine formula, each interface has
degree at most \(d\) in \(u\) and in \(\bar u\);
its radial density is therefore \(O(v^{-2})\,dv\)
at infinity. All integrals are absolutely convergent.
There are no states outside the original finite box.

If a frame moves with \(M\), differentiate the
actual kernels (3). The frame connection terms
cancel in the full integrated cyclic product,
since its product is \(D_0^{-1}BD_0\).
They are not discarded from a pointwise integrand
or from a restricted integration window.

## 2. A beta rotation puts each Cartan in the density

For \(s=Q\) or \(Q^{-1}\), put
\[
                       R_s(v)=
                  \left(\frac{1+v}{1+s v}\right)^{N+1}.
 \tag{9}
\]
On the original real sphere \(v=|u|^2\ge0\).
Its denominator does not vanish for \(N\ge3\).
The weighted beta moment is exactly
\[
 \int R_s(|u|^2)u^a\bar u^{\,b}\,d\nu_N(u)
          =\frac{\delta_{ab}s^{-a-1}}{\binom da}.
 \tag{10}
\]
Indeed the diagonal radial integral becomes
\(N\int_0^\infty v^a(1+s v)^{-N-1}dv\).
Make the substitution \(z=sv\). Its factor is
\(s^{-a-1}\). The ray of \(z\) can be rotated
back to the positive real ray: the intervening
sector has angle \(2\pi/N<\pi\), and never contains
the only pole \(z=-1\).
On an outer circular arc of radius \(R>2\), its
integral is \(O(R^{a-N})=O(R^{-1})\), even for
\(a=d\). The inner arc is \(O(\rho^{a+1})\).
Both vanish. This proves (10) with its orientation
and scalar, without an infinite occupation series.

Insert these weights at the interface \(u_0\) only,
and write \(v_j=|u_{0,j}|^2\). Define
\[
 \begin{split}
 \mathcal A_N(v)&=x_0^{-r}\prod_{j=1}^rR_Q(v_j),\\
 \mathcal B_N(v)&=x_0^{r}\prod_{j=1}^rR_{Q^{-1}}(v_j).
 \end{split}
 \tag{11}
\]
All other interfaces retain their original measure.
The factors in (10) are \(Q^{-|a|-r}\) and
\(Q^{|a|+r}\). Since \(x_0^2=Q^{-1}\),
\[
 x_0^{-r}Q^{-r}=x_0^r,\qquad
 x_0^rQ^r=x_0^{-r}.
 \tag{12}
\]
Thus finite composition gives the exact identities
\[
 \begin{split}
 \int\mathcal A_N\mathcal P_N\,d\boldsymbol\nu_N
                     &=\operatorname{Tr}(K_0B(e^\mu)),\\
 \int\mathcal B_N\mathcal P_N\,d\boldsymbol\nu_N
                     &=\operatorname{Tr}(K_0^{-1}B(e^\mu)).
 \end{split}
 \tag{13}
\]
Here \(K_0\) is the complete remaining Cartan at
\(M=1\), with eigenvalues \(x_0^rQ^{-|a|}\).
It commutes with every diagonal \(D_0\), so no
frame is left over in (13). The same literal
integrand \(\mathcal P_N\) occurs in both lines.

## 3. The whole meridian and its true first jet

The original source is
\[
 \Phi_N(\mu)=\operatorname{Tr}_{\rm full}
       \bigl((P_0\otimes K_{\rm r}(e^\mu)^{1-N})W(e^\mu)\bigr).
 \tag{14}
\]
R proves its meromorphic reduced expression
\[
 \Phi_N(\mu)=\operatorname{Tr}_{\rm r}
       \left(\frac{D_N(e^\mu)}
                    {D_N(e^\mu K_{\rm r}(e^\mu))}B(e^\mu)\right),
 \quad D_N(z)=\frac{z^N-z^{-N}}{z-z^{-1}}.
 \tag{15}
\]
The original finite left side is analytic at zero.
The actual remaining Cartan is \(e^{r\mu}K_0\),
and \(K_0^N=\varepsilon I\) on the finite tensor.
This is a matrix statement on physical integer
indices, not an off-grid clock substitution.
Combining (13) with (15) gives
\[
 \boxed{\quad
 \Phi_N(\mu)=
       \int\mathcal W_N(v,\mu)\mathcal P_N(\mu)\,
                                               d\boldsymbol\nu_N,
 \qquad
 \mathcal W_N=
 \frac{D_N(e^\mu)
       (e^{m\mu}\mathcal A_N-e^{-m\mu}\mathcal B_N)}
                    {2\varepsilon\sinh(mN\mu)} .
 \quad}
 \tag{16}
\]
It holds first away from the displayed poles and
then by the original analytic continuation. The
self-Cartan cases are included in this whole
identity.

Set
\[
 \mathfrak c_N=\frac{\mathcal A_N+\mathcal B_N}{2\varepsilon},
 \qquad
 \mathfrak d_N=\frac{\mathcal A_N-\mathcal B_N}{2\varepsilon m}.
 \tag{17}
\]
Since \(D_N(e^\mu)=\sinh(N\mu)/\sinh\mu\) is even
and has value \(N\) at zero,
\[
                \mathcal W_N=\mathfrak d_N/\mu+
                                     \mathfrak c_N+O(\mu).
 \tag{18}
\]
The rational factors (9) are smooth on the
original compact cycle. Finite matrices and
compactness justify integration of this Laurent
expansion and its fixed meridian derivatives.
Analyticity of (14) yields the specified residue
identity
\[
                  \int\mathfrak d_N\mathcal P_N(0)\,
                                            d\boldsymbol\nu_N=0.
 \tag{19}
\]
It is an integrated source identity, not a
pointwise cancellation.

On \(|\mu|<c/N\), \(0<c<\pi/m\), provided this collar
lies in the chosen analytic word and frame domain, the density
\[
 \mathcal W_N(v,\mu)\mathcal P_N(\mu)
                    -\mu^{-1}\mathfrak d_N(v)\mathcal P_N(0)
 \tag{20}
\]
has a removable singularity at zero and no other
meridian pole. By (19) its integral is still
the original source. The finite part is exactly
\[
 \boxed{\quad
 \Phi_N(0)=\int\left\{
       \mathfrak c_N\mathcal P_N(0)
       +\mathfrak d_N\partial_\mu\mathcal P_N(0)
                         \right\}d\boldsymbol\nu_N .
 \quad}
 \tag{21}
\]
The derivative includes the whole actual reduced
word, all scalars, and every moving-frame
connection. At \(M=1\), it equals the \(M\)
derivative. The frozen Cartan is not differentiated
a second time; its required meridian dependence
is already in \(e^{\pm m\mu}\) in (16).

## 4. The scalar normal is a unit at nonreal total spin moment

Complexify the selected interface to independent
\(z_j,w_j\), and put
\[
             v_j=z_jw_j,\qquad t_j=\frac{v_j}{1+v_j},
             \qquad T=\sum_{j=1}^r t_j,\qquad c_0=2\pi i .
 \tag{22}
\]
Fix a compact affine chart with \(1+v_j\ne0\).
The \(t_j\)'s are bounded there. For sufficiently
large \(N\), all \(1+Q^{\pm1}v_j\) are nonzero,
and the logarithm near one gives, uniformly
with all fixed holomorphic derivatives,
\[
 \begin{split}
 \mathcal A_N&=(-1)^r e^{-c_0T}(1+O(N^{-1})),\\
 \mathcal B_N&=(-1)^r e^{c_0T}(1+O(N^{-1})),\\
 \mathfrak d_N
       &=-\frac{i(-1)^r}{\varepsilon m}
                              \sin(2\pi T)+O(N^{-1}).
 \end{split}
 \tag{23}
\]
For example
\(R_Q=(1+(Q-1)t)^{-N-1}\); expansion of this
exact expression proves the first line,
including the actual \(N+1\) and \(x_0^{-r}\).
Their finite half shifts remain in (11), not
in a reset amplitude.

If \(|\Im T|\ge\delta>0\) on that compact set,
then
\[
                      |\sin(2\pi T)|\ge\sinh(2\pi\delta).
 \tag{24}
\]
Equations (23)--(24) give a uniform positive
lower bound on \(|\mathfrak d_N|\) for all
sufficiently large \(N\). Its reciprocal and
all fixed derivatives are uniformly bounded
on smaller compact buffers. Thus it is an
actual scalar normal unit on this complex
spin chart, not merely a nonzero principal
symbol.

The common moment here is independent of
the diagonal frames. Indeed their Cartan
kernel is unchanged, and its exact normalized
one-head symbol is
\[
       x_0\left(\frac{1+Q^{-1}zw}{1+zw}\right)^d
                   =-e^{-c_0t}(1+O(N^{-1})).
 \tag{25}
\]
This identifies the corresponding principal
clock without taking any off-grid \(N\)-th
power of it. G's resolved total-lowering-zero
map has \(K_\Sigma=x_{\rm cl}K_{\rm r}\).
At a complete loxodromic geometric total,
\(|K_{\rm r}|\ne1\); on a spin chart actually
matched to that map,
\(K_{\rm r}=(-1)^r e^{-c_0T}\) therefore implies
\(\Im T\ne0\). The scalar unit applies whenever
that chart matching and its nonincidence
conditions have been supplied. It is not a
new assertion of whole-word kernel coverage.

## 5. Scope of the exact adapter

All formulas use one finite spin resolution and
one cyclic list of actual frames. In particular
hybrid choices of physical and factorial heads
need no asymptotic passage through a Bargmann
kernel to use (16) or (21). Every finite
occupation cap is already present in (4).

The rotated incidence divisors
\(1+Q^{\pm1}z_jw_j=0\) of (11) remain part of
the exact complex density. Although they avoid
each fixed compact nonincident chart for large
\(N\), their possible global contour currents
are not discarded. The beta rotation proves
the original cycle identity; it does not
transport an arbitrary chosen geometric
window through these divisors.

Likewise (19) need not hold on an angular
subchain. Its restricted pole coefficient
and all frame-connection currents must then
be retained. A separately prescribed scalar
line multiplies the whole original expression,
before its required finite part or derivative.
No rate or nonvanishing is assigned to that
line here.

The conclusion is an exact common-spin source
dual and a local scalar normal unit. Neither
the angular pairing, its geometric coefficient,
nor the full original-source lower bound is
proved by this adapter.

## Complete proof-source pins

* R: notes/research_actual_reduced_braid_source.md, 330 lines,
  SHA256 9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.
* G: notes/research_actual_reduced_braid_critical_scheme.md, 564 lines,
  SHA256 ddddcd9bf75f35afdf3e5de0c03323acee2c66e624db36142c2344ef729a977a.

Both complete directs were freshly read nontruncated in the
active author sequence and retained unchanged. Every used
implication was checked. The beta rotation, cyclic frame
algebra, and source expansion were proved above from the
actual finite formulas. No mathematical programs, tests,
or edits to frozen or public files were used.
