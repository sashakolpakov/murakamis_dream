# Endpoint-product transfers on forests and a whole microscopic current gap

Private written proof, 16 November 2026.

The original unit-leaf identity permits one transfer of any fixed
endpoint product with subexponential cost. A receiving vertex keeps
every transformed factor, and is subsequently consumed by an isolated
trace or by a clean zero-leaf evaluation. It is not turned again.
This rule gives a strictly larger forest certificate than the
previous certificate with static marked vertices, and bounds the
whole corresponding microscopic current.

The proof uses exact source reductions and the whole-product unit-turn
upper bound. It makes no assumption about the unit-turn norm on an
arbitrary subexponential coupon.

## 1. Original forest source and permitted reductions

Retain
\[
 q=e^{\pi i/N},\quad D=N-1,\quad\eta=(-1)^D,\quad
 \kappa=q^{D^2/2},\quad c_a=2\cos((2a+1)\pi/N),
\]
\[
 P_N(Z)=2T_N(Z/2)+2,\qquad
 \mathcal A_N=\mathbb C[Z]/(P_N),\qquad
 K_N(w,Z)=\sum_{j=0}^{D}e_j(w)e_j(Z),
\]
\[
 \phi_N(e_i e_j)=\mathbf1_{i+j=D},\quad
 Te_j=e_{D-j},\quad
 U_\sigma=\kappa^\sigma TR^{-\sigma}T
                      \quad(\sigma=\pm1).
 \tag{1}
\]
Here \(e_j(Z)=S_j^{-2}\prod_{a<j}(c_a-Z)\),
\(S_j=\prod_{a=1}^j2\sin(a\pi/N)\), and \(S_0=1\).
For an integer \(n\), write \(V_n=\kappa^nTR^{-n}T\);
thus \(U_\sigma=V_\sigma\).
These are the original kernel, full Frobenius trace and signed
crossing carriers. The notation \(\operatorname{can}\) denotes
the ordinary representative of degree at most \(D\) in the
traced variable.

Let \(F=(V,E)\) be a fixed finite forest, all of whose vertices
are traced, with no additional untraced kernel incidences.
Fix integer powers \(n_v\) and original endpoint products
\[
 Q_{v,N}(Z;\boldsymbol\alpha)
       =\prod_{i=1}^{r_v}K_N(2\cosh(\alpha_{v,i}/N),Z),
 \qquad |\alpha_{v,i}|\le A<\infty .
 \tag{2}
\]
An empty product is one. The source is exactly
\[
 Z_{F,N}(\boldsymbol\alpha)
 =\left(\prod_{v\in V}\phi_N^{(v)}\right)
  \left[\prod_vR(z_v)^{n_v}Q_{v,N}(z_v)
                     \prod_{vw\in E}K_N(z_v,z_w)\right].
 \tag{3}
\]
All products are ordinary products before their original trace.
Endpoint parameters may be shared between incidences; they are
retained as the same parameters throughout.

A reduction certificate consists of a finite sequence on the
current forest and current integer powers. At each surviving
vertex keep a list of received transformed factors, initially empty.
The allowed operations are the following.

1. Remove an isolated vertex, with any current power, original
   endpoint product, and list of received factors.
2. Remove a leaf \(v\) whose current power is
   \(\sigma\in\{1,-1\}\), provided its received list is empty.
   Change the power of its neighbor \(w\) to \(n_w-\sigma\).
   If \(r_v>0\), append the factor
   \[
                  S_{v,N}=U_\sigma\operatorname{can}Q_{v,N}
   \tag{4}
   \]
   to the list at \(w\), recording the actual current sign
   \(\sigma=\sigma_v\). If \(r_v=0\), append nothing:
   \(U_\sigma1=1\).
3. Remove a zero-power leaf \(v\) and its neighbor \(w\),
   provided \(r_v=0\) and the received list at \(v\) is empty.
   Remove all edges incident to these two vertices. Other powers
   and received lists are unchanged.

The sequence must end at the empty forest. It is fixed independently
of \(N\) and the endpoint parameters. In particular a vertex which
has received a factor (4) is not eligible for either leaf operation.
It may receive further factors, be removed when isolated, or be
consumed as the neighbor in operation 3.

Every factor in a list is tagged by an original vertex which was
removed by operation 2. It is formed from that vertex's original
product (2), not from a product containing other received factors.
At a surviving vertex \(w\), the exact current coupon is
\[
       \widetilde Q_{w,N}(Z)
           =Q_{w,N}(Z)\prod_{v\in\mathcal L_w}S_{v,N}(Z),
 \tag{5}
\]
where \(\mathcal L_w\) is its list. The original products and
all signs in the received factors are thus specified without
any analytic choice or approximation.

## 2. Exact leaf identities and the zero-step scalar

The all-degree unit identity is
\[
 \phi_N^{(z)}[K_N(z,w)f(z)]=(Tf)(w),\qquad
                    T(R^\sigma P)=R^{-\sigma}U_\sigma P
                       \quad\hbox{in }\mathcal A_N .
 \tag{6}
\]
It is valid for every canonical \(P\), including its first
normal data, not only for a low Newton-degree coupon.
At a traced neighbor, (6) proves operation 2 exactly, with
no additional scalar. The neighbor's other edges and its
entire coupon (5) stay inside the original trace.
Its received factors are multiplied there with their full
product-rule normals. Since the neighbor is traced, the
canonical equality in (6) suffices; no equality of an
unreduced off-spectrum product is being asserted.

The exact zero-leaf identities are
\[
 T1=e_D,\qquad
 \phi_N(e_D R^n A)=\kappa^n A(c_0),\qquad
 K_N(c_0,Z)=1,\qquad Q_{v,N}(c_0)=1.
 \tag{7}
\]
The normal in the middle expression is consumed by \(e_D\)
inside the full trace. Operation 3 therefore contributes
the scalar
\[
                    \kappa^{n_w}\widetilde Q_{w,N}(c_0).
 \tag{8}
\]
All other incident kernels at \(w\) become one by actual
evaluation at \(c_0\).

In contrast with the static-product certificate, the coupon
in (8) need not equal one. Its exact value is
\[
 \boxed{\quad
 \kappa^{n_w}\widetilde Q_{w,N}(c_0)
   =\kappa^{\,n_w+\sum_{v\in\mathcal L_w}\sigma_v}
          \prod_{v\in\mathcal L_w}
                   \phi_N(R^{\sigma_v}Q_{v,N}).
 \quad}                                                   \tag{9}
\]
Indeed \(T f(c_0)=\phi_N(f)\) and \(R(c_0)=\kappa\);
evaluating (6) gives
\[
          (U_\sigma\operatorname{can}Q)(c_0)
                            =\kappa^\sigma\phi_N(R^\sigma Q).
 \tag{10}
\]
Together with \(Q_{w,N}(c_0)=1\), this proves (9).
If any scalar vanishes, the corresponding whole source is
zero; no division by it is made. Shared endpoint parameters
in the factors of (9) remain shared with the surviving source.

Equations (6)--(10) hold at both parities and at \(N=2\).
The asymptotic estimates below may discard finitely many
levels, without changing any of these identities.

## 3. Subexponential closure under the certificate

The original endpoint-product bound gives
\[
                \|Q_{v,N}\|_{\mathbb R}\le C_A N^{p_A}
 \tag{11}
\]
for every fixed product and bounded complex parameter disk.
Its ordinary degree is at most \(r_vD\). The turned-product
theorem, applied with \(n=\sigma=\pm1\) and
\(\mathcal I_\sigma=0\), gives
\[
 \limsup_{N\to\infty}\frac1N
       \log\left(1+\sup_{|\boldsymbol\alpha|\le A}
                      \|S_{v,N}\|_{\mathbb R}\right)=0.
 \tag{12}
\]
The norm here is that of the canonical polynomial (4), whose
degree is at most \(D\). Thus a current coupon (5) has
ordinary degree at most \((r_w+|\mathcal L_w|)D\);
its real norm is bounded by the product of (11)--(12).
No coefficientwise estimate of a growing Newton expansion
is needed.

For precision define
\[
 b_N(A)=\max\left\{1,\ 
  \sup_{\substack{v:r_v>0,\ \sigma=\pm1\\
                   |\boldsymbol\alpha_v|\le A}}
      \|U_\sigma\operatorname{can}Q_{v,N}\|_{\mathbb R}\right\}.
 \tag{13}
\]
The maximum over an empty set contributes nothing.
There are only finitely many original vertices and signs,
so \(\log b_N(A)=o(N)\).

For an ordinary coupon \(Q\) of degree at most \(dD\),
the exact original trace and crossing jets give
\[
                 |\phi_N(R^n Q)|
       \le C_d(1+|n|)N^3\|Q\|_{\mathbb R}.
 \tag{14}
\]
To recall the full-normal estimate, the trace is
\[
 \phi_N(H)=\eta\sum_{\text{double }a}
          [(4-c_a^2)H'(c_a)-c_aH(c_a)]
               +\mathbf1_{N\ {\rm odd}}H(-2).
 \tag{15}
\]
The crossing has unit-modulus values and
\(|(R^n)'(c_a)|\le |n|N^2/8\). Markov bounds
\(\|Q'\|_{\mathbb R}\le(dD)^2\|Q\|_{\mathbb R}/2\).
Inserting the actual product derivative into (15) proves
(14). This applies when the ordinary degree exceeds \(N\);
it estimates the actual jets, rather than changing them.
In particular every original trace in (9) is polynomially
bounded by (11),(14).

**Theorem 1.** If the forest source (3) has a certificate of
Section 1, then, uniformly on bounded complex endpoint
parameter sets,
\[
                |Z_{F,N}(\boldsymbol\alpha)|
                       \le C N^p b_N(A)^{t},
 \qquad
 \limsup_{N\to\infty}\frac1N
    \log\left(1+\sup_{|\boldsymbol\alpha|\le A}|Z_{F,N}|\right)=0.
 \tag{16}
\]
Here \(t\le|V|\) is the number of operations 2 at vertices
with \(r_v>0\). Constants depend only on the fixed forest,
powers, endpoint multiplicities, parameter bound and certificate.
All fixed endpoint-parameter derivatives have the same rate.

*Proof.* Follow the fixed certificate while retaining (5)
at every surviving vertex. Operation 2 is the exact source
identity (6), and adds precisely the factor (4).
Operation 3 has the exact scalar (9), with polynomial
bound just proved, and evaluates every other incident
kernel to one. An isolated vertex has its entire coupon
(5) and current crossing inside one trace; (11)--(14)
bound it by a polynomial times
\(b_N(A)^{|\mathcal L_w|}\).
All current integer powers have size at most
\(\max_v|n_v|+|V|\).

Each received factor is created once and consumed once.
Thus multiplying the estimates along the certificate gives
the first inequality in (16), allowing unused factors
\(b_N\ge1\) for lists consumed by operation 3.
It is a bound on the original coherent trace, not on
independent replacements for its neighboring factors.
Taking logarithms and using (13) proves the second assertion.
Cauchy's formula on a larger fixed complex parameter
polydisk proves the derivative assertion. \(\square\)

Fixed derivatives with respect to the actual microscopic
spectral parameters \(w_i\) also retain this rate. The
source is even and entire in each \(\alpha_i\), so it
descends holomorphically to \(\xi_i=\alpha_i^2\).
On buffered bounded disks,
\[
 N^2(w_i-2)=2N^2(\cosh(\alpha_i/N)-1)
                           =\xi_i(1+O_A(N^{-2}))
 \tag{17}
\]
has a uniformly regular holomorphic inverse for large \(N\).
Cauchy's formula in this coordinate costs only \(N^2\)
per \(w_i\) derivative, including at \(\alpha_i=0\).
All internal spectral normals were already kept exactly
by (6),(7),(15); (17) concerns ordinary exterior parameters.

This certificate contains every static marked certificate:
an unmarked unit leaf has \(r_v=0\) and transmits no factor;
an unmarked zero leaf satisfies operation 3; isolated
vertices are unchanged. The containment is strict. For
example, take a star with at least two leaves, each carrying
a nonempty endpoint product and current power \(+1\) or
\(-1\), and give its center any integer power and endpoint
product. The static marked rules have no initial move.
Here all leaves can be removed by operation 2, after
which the center is isolated and (14) consumes its whole
product of received factors. This is a structural family
of certificates of arbitrary fixed valence, not a statement
about an individual filling.

## 4. Exact application to the whole microscopic current

Use the original circle tree \(G\), selected vertices \(S\),
outside vertices \(B\), unit charges, and fixed integer
powers. Assume \(S\) is nonempty and every selected vertex
has an original incidence. Choose a nonempty current set \(C\subseteq S\)
which contains every selected vertex incident to \(B\).
Put \(Y=S\setminus C\). Its surviving graph \(G[Y]\) is
a closed forest with no extra untraced kernel incidences.
Fix
\[
       0\le h_v\le\alpha_v/N,\qquad 0\le\alpha_v\le A<\pi,
       \qquad w_v=2\cosh h_v\quad(v\in C).
 \tag{18}
\]
The actual original endpoint products at survivors are
\[
 Q_{y,N,\mathbf h}(z)
          =\prod_{\substack{v\in C\\vy\in E}}K_N(w_v,z).
 \tag{19}
\]
The same \(h_v\) occurs at all its incidences. Retain also
\[
 D_{C,N}(\mathbf h;\mathbf z_B)
 =\prod_{\substack{vv'\in E\\v,v'\in C}}K_N(w_v,w_{v'})
       \prod_{\substack{vb\in E\\v\in C,\ b\in B}}K_N(w_v,z_b).
 \tag{20}
\]
Internal \(C\)--\(C\) kernels are part of this expression.

With the original carrier
\[
 C_{N,n}=e^{\pi i nD^2/(4N)},\qquad
 \rho_{N,n,1}(h)
  =\frac{2i\eta N^2C_{N,n}}{\pi}
     \frac{\sinh h\ e^{inN(\pi^2-h^2)/(4\pi)}
                          \sinh(nNh/2)}{4\cosh^2(Nh/2)},
 \tag{21}
\]
the full current is exactly
\[
 \begin{split}
 I_{C,N}(\mathbf z_B)=
 \int_{\prod_{v\in C}[0,\alpha_v/N]}
 &\prod_{v\in C}\{\rho_{N,n_v,1}(h_v)\,dh_v\}\,
       D_{C,N}(\mathbf h;\mathbf z_B)\\
 &{}\times
 \left(\prod_{y\in Y}\phi_N^{(y)}\right)
 \left[\prod_{y\in Y}R(z_y)^{n_y}Q_{y,N,\mathbf h}(z_y)
                    \prod_{yy'\in E(G[Y])}K_N(z_y,z_{y'})\right].
 \end{split}                                             \tag{22}
\]
Its coefficient in the full inclusion--exclusion formula,
when that formula is used, remains \((-1)^{|C|+1}\).
No band projection, carrier change or individual-edge
replacement has been made.

**Theorem 2.** Suppose \(G[Y]\), with its original products
(19) and powers, has a certificate of Section 1.
Then for real outside colors \(z_b\in[-2,2]\),
\[
 \limsup_{N\to\infty}\frac1N
       \log\left(1+\sup_{\mathbf z_B}|I_{C,N}(\mathbf z_B)|\right)=0.
 \tag{23}
\]
All fixed ordinary outside derivatives obey the same bound.
Empty \(Y\) is allowed, with its empty certificate.

*Proof.* In (19) each microscopic parameter is \(Nh_v\in[0,A]\).
The uniform bound (16), before any parameter identifications,
therefore bounds the entire surviving full trace in (22)
by \(\exp(o(N))\), uniformly in every integration variable.
The original microscopic current estimates give
\[
 \int_0^{\alpha_v/N}|\rho_{N,n_v,1}(h)|\,dh\le C,\qquad
 |D_{C,N}(\mathbf h;\mathbf z_B)|
                          \le C N^{2(e_C+b_{CB})}.
 \tag{24}
\]
Here \(e_C\) counts internal \(C\)-edges and \(b_{CB}\)
counts \(C\)--outside edges. The first estimate follows
also directly from (21): \(N^2,\sinh h,dh\) cost
\(N^2,N^{-1},N^{-1}\), and all other factors are bounded
for \(Nh\le A\). The second is the full-kernel
microscopic estimate, including the internal edges.
Equations (22)--(24) prove (23).

Every outside variable occurs in its original ordinary
polynomial factor, of degree at most \(d_bD\), where
\(d_b\) is its included incidence degree. Markov's
inequality on the real outside cube costs a polynomial
for every fixed derivative. No outside variable is
canonically reduced. This proves the last assertion.
\(\square\)

Suppose the supplied original parent has positive unit-charge
geometry at complete outside colors, with calibrated action
\[
             M_G=e_GM_\infty-\mathcal E(z_0)/\pi>0,
                    \qquad M_\infty=4G_{\rm Cat}/\pi .
 \tag{25}
\]
Here \(e_G\) counts the included original edges,
\(\mathcal E(z_0)\) is the parent's calibrated square energy,
and \(G_{\rm Cat}\) is Catalan's constant.
The static-current source proves this strict positivity
from its strict interior square energies. Then (23) gives
the genuine strict parent gap
\[
          \limsup_{N\to\infty}N^{-1}\log|I_{C,N}|
                                      \le0<M_G
 \tag{26}
\]
at complete outside colors, including fixed outside normals.
For any \(0<\delta<M_G\), the actual current is eventually
bounded by \(\exp(N(M_G-\delta))\), with a fixed
multiplicative constant if desired. A finite collection
of certified current sets has the same conclusion.

The ordinary outside continuation is also explicit:
\[
 |I_{C,N}(\{-2\cos u_b\})|
       \le\exp\left\{o(N)+N\sum_{b\in B}d_b|\Im u_b|\right\}.
 \tag{27}
\]
To see this, bound its tensor cosine coefficients by the
real-cube supremum, use the polynomial number of modes,
and keep the maximum frequency \(d_bD\) in each variable.
The same proof after fixed outside derivatives applies.
A fixed strip satisfying
\(\sum_b d_b|\Im u_b|\le M_G/2\) retains a strict parent gap.

## 5. The exact operation still outside the certificate

If a receiving vertex were itself removed as a unit leaf,
its next transmitted coupon would be
\[
        U_\tau\operatorname{can}
              \left(Q_{w,N}\prod_{v\in\mathcal L_w}
                           U_{\sigma_v}\operatorname{can}Q_{v,N}\right).
 \tag{28}
\]
The argument above supplies no bound for (28). A
subexponential real norm of its input does not authorize
another application of the endpoint-product theorem.
Even when \(Q_{w,N}=1\) and the list has one factor,
the exact group law gives
\[
                    U_\tau U_\sigma Q=V_{\tau+\sigma}Q.
 \tag{29}
\]
Opposite signs return \(Q\); equal signs are a two-turn
operator. The certificate does not silently replace either
case by a fresh endpoint product. A separately specified
cancellation rule could use the first identity when its
entire hypothesis holds, but is not needed here.

Thus this proof covers the entire current for its explicit
structural class, while leaving (28), macroscopic heights,
other current patterns and the nonzero full geometric
coefficient unresolved. Arbitrary joint spectators and
additional untraced kernel incidences are not inserted
into the forest theorem.

## 6. Direct sources

The three complete direct sources were read at these
unchanged versions, with the used implications checked:

* [Turned endpoint-product upper rate](research_turned_endpoint_product_characteristic_upper_bound.md),
  SHA256 5e594fa40c1ab70b72a0c1b85748182e33850675a45ed6ea42f2c20349831b2a:
  uniform bounded-complex-parameter rate \(2\mathcal I_n\),
  in particular the actual unit-turn rate zero, with all normals.
* [Static marked forest and current](research_marked_forest_full_endpoint_current_gap.md),
  SHA256 1acab0d1bc65bbc2ff318e54adcc9d99722129f2b89624720550465e9402b652:
  original full forest trace, endpoint-product norm,
  exact zero-leaf evaluation and crossing jets,
  microscopic current and outside bounds, parent positivity.
* [All-degree original unit turn](research_full_endpoint_unit_turn_identities.md),
  SHA256 e2f69aaff28080b9dd9e11365ce18d68a9d738667917204714556681c50789e8:
  full-algebra identity (6), canonical placement and the
  original signed operator normalization.

Only written mathematics and source-text/hash reads were
used. No mathematical program, numerical experiment, test
or build was run. Adopted files and public manuscripts
remain unchanged.
