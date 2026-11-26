# First-order Gaussian transport with the original Hermite closing

Private written proof, 15 November 2026.

The original even crossing Gaussian has a first-order shift equation
on the doubled Laurent spectrum. Its failure to close around that
spectrum is purely normal, and a cut localizes the failure at one
node. This is the one-sided form of the existing endpoint Ward
identity. The additional construction here concerns the closing:
two perfect extensions at odd levels permit arbitrary one-sided
transport with a polynomial cost independent of the number of steps.
They agree with the original closing on its physical invariant
subalgebra, and inversion exchanges the two extensions.

The estimate is relative to the full physical jet norm of the
spectator. It does not estimate that spectator at the hyperbolic-volume
rate or prove a nonzero original scalar.

## 1. The doubled spectrum and the odd fixed point

Fix \(N\ge2\), and write
\[
 D=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \eta=(-1)^D,\quad \rho=q-q^{-1},\quad \kappa=q^{D^2/2}.
 \tag{1}
\]
All powers of \(q\) use the displayed logarithm. Set
\[
 \mathcal B_N=\mathbb C[w,w^{-1}]/((w^N+1)^2),\qquad
 \delta=w^N+1,\qquad
 (Uh)(w)=h(Qw),\qquad (\iota h)(w)=h(w^{-1}).
 \tag{2}
\]
These are well-defined algebra automorphisms, with
\[
 \delta^2=0,\quad U\delta=\delta,\quad
 U^N=1,\quad \iota\delta=-\delta,\quad
 \iota U\iota=U^{-1}.
 \tag{3}
\]
For the fourth identity, \(w^N=-1+\delta\) has inverse
\(-1-\delta\).

Let \(w_j=q^{2j+1}\), \(0\le j<N\). An element is specified by
its values \(h_j\) and first logarithmic jets
\[
 \dot h_j=\left.w\frac{d\widetilde h}{dw}\right|_{w=w_j},
 \tag{4}
\]
where \(\widetilde h\) is any Laurent representative. Both are
well-defined. Differentiation in (4) is a jet evaluation, not a
derivation of the quotient: \(w\partial_w\) does not preserve the
ideal \(((w^N+1)^2)\). Let \(p_j\) be the local idempotent with
value one at \(w_j\), zero at the other nodes, and zero first jets
everywhere. Thus \(Up_j=p_{j-1}\), with indices modulo \(N\), and
\[
 (\delta p_j)_a=0,\qquad
 \dot{(\delta p_j)}_a=-N\mathbf1_{a=j}.
 \tag{5}
\]

**Lemma 1.** Substitution \(z=w+w^{-1}\) identifies the original
full algebra with the inversion invariants:
\[
 \mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2)
                  \ \simeq\ \mathcal B_N^\iota.
 \tag{6}
\]

**Proof.** The relation pulls back to \(w^{-N}(w^N+1)^2\).
Away from \(w=\pm1\), the map to \(z\) has nonzero derivative.
An inversion pair of double Laurent nodes therefore has invariant
algebra equal to one double Casimir node. At even levels all nodes
occur in such pairs. At odd levels the only fixed node is \(w=-1\).
In its local coordinate \(w=-e^y\), \(y^2=0\), inversion is
\(y\mapsto-y\). Its invariant algebra consists only of constants,
and \(z=-2\cosh y=-2\) there. This is precisely the original
simple Casimir node \(-2\). The local identifications exhaust both
algebras and prove (6). In particular an invariant element has
zero logarithmic jet at the odd fixed node. \(\square\)

## 2. The first-order defect and its exact propagation

Let \(m\in2\mathbb Z\), and let \(g_m\in\mathcal B_N^\iota\)
be the pullback of the original normalized crossing \(r_N^m\),
where \(R=\kappa r_N\). The full Hermite Gaussian identity gives
\[
 (g_m)_j=\nu_j^m,\qquad
 \dot{(g_m)}_j=-\frac m2(D-2j)\nu_j^m,\qquad
 \nu_j=(-1)^j q^{j(j+1)}.
 \tag{7}
\]
At the odd fixed node the second expression is zero. These are
the original crossing values and normals, not a newly chosen
solution of a reduced recurrence.

**Proposition 2.** In the full doubled algebra,
\[
 \boxed{\quad(U-q^m w^m)g_m=m\delta p_D.\quad}
 \tag{8}
\]
For every integer \(k\), put
\[
 a_k=q^{mk^2}w^{mk},\qquad
 L_k=\sum_{j=0}^{N-1}\left\lfloor\frac{j+k}{N}\right\rfloor p_j.
\]
Then
\[
 \boxed{\quad U^k g_m=a_k g_m(1+m\delta L_k).\quad}
 \tag{9}
\]

**Proof.** Use the original unwrapped logarithms
\(x_j=(2j+1)\pi i/N\) and \(\hbar=2\pi i/N\). Their Gaussian
\[
 G_m(x)=q^{-mD^2/4}
          \exp\!\left(\frac{m(x-\pi i)^2}{2\hbar}\right)
\]
satisfies \(G_m(x+k\hbar)=a_k(e^x)G_m(x)\), since \(m\) is
even. Write \(j+k=r+N\ell\), \(0\le r<N\). The Gaussian value
at \(x_{j+k}\) equals its value at \(x_r\): equivalently,
\(\nu_{r+N}/\nu_r=-1\), whose \(m\)-th power is one. Its
logarithmic derivative divided by that value exceeds the actual
derivative at \(x_r\) by \(mN\ell\). Multiplication by
\(1+m\delta L_k\) subtracts exactly that amount, by (5).
This proves equality of all values and first jets in (9), for
positive and negative \(k\). For \(k=1\), \(L_1=p_D\), and
\((a_1g_m)(w_D)=1\); the correction is exactly \(m\delta p_D\).
\(\square\)

The uncorrected multiplier has the full-loop product
\[
 \prod_{j=0}^{N-1}q^m(Q^jw)^m=w^{mN}=1-m\delta.
 \tag{10}
\]
The constant factor is one since \(m\) is even. If \(m\ne0\),
any full-algebra solution of \(Uf=q^mw^mf\) must satisfy
\(\delta f=0\), so has zero value at every node. It cannot be a
unit. On the reduced node set the recurrence instead has a
one-dimensional solution space, fixed by its value at any node.

Equation (9) repairs (10): at \(k=N\), \(L_N=1\), and the
factors \(1-m\delta\) and \(1+m\delta\) cancel. For
\(0\le k\le N\), \(L_k\) is the projector onto nodes whose
shift crosses the cut. No endpoint term is discarded.

The corrected multiplier
\[
 \widehat a=q^mw^m(1+m\delta p_D)=q^mw^m+m\delta p_D
 \tag{10a}
\]
has cyclic product one. The product of its correction factors is
\(1+m\delta\sum_jp_j=1+m\delta\), which cancels (10).
All unit solutions of \(Ug=\widehat a g\) are exactly
\(g=g_m(a+b\delta)\), with \(a\ne0\). They form a torsor
under \((\mathbb C[\delta]/(\delta^2))^\times\): multiplication
by this group is free and transitive. Indeed the ratio of
two solutions is \(U\)-invariant, and a \(U\)-invariant
element has constant values and constant first jets, hence lies
in \(\mathbb C[\delta]/(\delta^2)\). Inversion invariance
forces \(b=0\), by (3). The normalization \(g(w_0)=1\)
then forces \(a=1\). Thus the retained current, inversion and
original normalization determine the full Gaussian uniquely.
This elementary cyclic descent concerns the filling factor;
it makes no assertion about its subsequent geometric turn.

Apply inversion to (8) and add. The two cut normals have the same
Casimir derivative at \(c_0=q+q^{-1}\), giving
\[
 (U+U^{-1}-q^m(w^m+w^{-m}))g_m
                         =\frac{mN}{\rho}\Xi_0(z).
 \tag{11}
\]
Their logarithmic derivatives at \(w_0,w_D\) are \(mN,-mN\);
those of \(z\) are \(\rho,-\rho\). Thus (11) is exactly the
archived even signed Ward identity. The spectral shift \(U\)
is not the geometric quarter-turn of the Newton algebra.

## 3. The original trace and its two odd-level extensions

Put \(t(w)=w-w^{-1}\), and define
\[
 \Lambda(h)=-\frac\eta2\sum_{j=0}^{N-1}\dot{(th)}_j.
 \tag{12}
\]
This is inversion-invariant and restricts under (6) to the original
closing \(\phi_N\). Indeed an inversion pair for \(h=f(z)\) contributes
\[
 -\eta\{c f(c)+(c^2-4)f'(c)\}
       =\eta\{(4-c^2)f'(c)-cf(c)\}.
\]
At the odd fixed node, \(t=0\), \(\dot t=-2\), and \(\eta=1\),
so its contribution is \(f(-2)\). These are the original
double-node normals and simple-node value with their exact factors.

At even levels \(t\) is a unit. At odd levels it is not:
the pairing \(\Lambda(ab)\) has precisely the one-dimensional
kernel of pure normals at \(w=-1\). This prevents an adjoint for
\(U\) on all of \(\mathcal B_N\). If \(\xi_*\) has zero values
and logarithmic jet one only at the fixed node, then
\(\Lambda(\xi_*A)=0\) for every \(A\). But \(U\xi_*\) is
supported at the nonfixed node \(-Q^{-1}\), where \(t\ne0\),
and \(\Lambda(U\xi_*)\ne0\). Hence no map \(V\) satisfies
\(\Lambda(AUf)=\Lambda(fVA)\) for all \(A,f\).

For odd \(N\), let \(p_*=p_{(N-1)/2}\), and put
\[
 t_+=t+p_*,\qquad t_-=t-p_*,\qquad
 \Lambda_\pm(h)=-\frac\eta2\sum_j\dot{(t_\pm h)}_j.
 \tag{13}
\]
At even levels use \(t_+=t_-=t\) and
\(\Lambda_+=\Lambda_-=\Lambda\).

**Proposition 3.** Both pairings \(\Lambda_\pm(ab)\) are perfect.
Both functionals agree with the original trace on
\(\mathcal B_N^\iota\), and
\[
 \Lambda_+\circ\iota=\Lambda_-,\qquad
 \tfrac12(\Lambda_++\Lambda_-)=\Lambda.
 \tag{14}
\]
For every integer \(k\), the exact one-sided adjoint is
\[
 V_{\pm,k}A=t_\pm^{-1}U^{-k}(t_\pm A),\qquad
 \boxed{\quad\Lambda_\pm(AU^k f)
                  =\Lambda_\pm(fV_{\pm,k}A).\quad}
 \tag{15}
\]
It obeys \(V_{\pm,k}V_{\pm,l}=V_{\pm,k+l}\) and
\(V_{\pm,N}=1\).

**Proof.** Each value of \(t_\pm\) is nonzero. In local value/jet
coordinates the functional is a nonzero constant times
\((\dot t_\pm)_j h_j+(t_\pm)_j\dot h_j\). Its product-pairing
matrix has determinant a nonzero multiple of \(-(t_\pm)_j^2\).
The direct product of these local pairings is therefore perfect.
For invariant \(h\), the added term in (13) is proportional to
\(\dot h_*=0\), proving agreement with \(\phi_N\). Inversion
negates logarithmic jets, fixes \(p_*\), and sends \(t_+\) to
\(-t_-\); these facts prove (14).

For (15), permute the nodes by \(w\mapsto Q^kw\) in the sum of
first jets on its left. Logarithmic jets commute with that
substitution. The resulting summand is the first jet of
\(U^{-k}(t_\pm A)f=t_\pm(V_{\pm,k}A)f\), proving the identity.
The group identities follow by cancellation of adjacent
\(t_\pm,t_\pm^{-1}\). \(\square\)

These extend the original closing rather than replace it on
physical sources. If transport creates noninvariant spectators,
the chosen extension must remain in every subsequent identity.
Interchanging the extensions without the inversion in (14) can
change the answer. The auxiliary normal at the odd fixed point
is not a new Casimir normal of the simple node.

## 4. Polynomial cost without accumulation over steps

Use the submultiplicative physical jet norm
\[
 \|h\|_N=\max_j\left(|h_j|+\frac{|\dot h_j|}{N}\right).
 \tag{16}
\]
Both \(U\) and inversion are isometries, and
\[
 \|t_\pm\|_N\le3,\qquad \|t_\pm^{-1}\|_N\le N,\qquad
 \|V_{\pm,k}\|\le3N\quad(k\in\mathbb Z).
 \tag{17}
\]
At nonfixed nodes,
\(|t_j|=2|\sin((2j+1)\pi/N)|\ge4/N\) and
\(|\dot t_j|\le2\). The inverse has jet
\(-\dot t_j/t_j^2\), giving norm at most
\(N/4+N/8=3N/8\) there. At the odd fixed node the modified
value is \(\pm1\), its jet is \(-2\), and the inverse norm is
\(1+2/N\le N\) for odd \(N\ge3\). These prove (17), using
the single conjugation (15), not \(|k|\) separate bounds.

The original Gaussian and its inverse obey
\[
 \|g_m\|_N,\ \|g_m^{-1}\|_N\le1+|m|/2.
 \tag{18}
\]
This follows directly from (7). All powers of the weighted shift
\(C_m=M_{g_m}^{-1}UM_{g_m}\) therefore have norm at most
\((1+|m|/2)^2\). Here \(M_g\) means multiplication by \(g\).
Its multiplier is the actual cut-corrected cocycle
\[
 C_m=(q^mw^m+m\delta p_D)U,
\]
by (8), not the inconsistent multiplier (10).

The closing itself satisfies
\[
 |\Lambda_\pm(h)|\le N(N+1)\|h\|_N.
 \tag{19}
\]
Indeed \(|t_{\pm,j}|\le2\) and \(|\dot t_{\pm,j}|\le2\);
the product rule in (12)--(13) proves this. The identities hold
coefficientwise with arbitrary ordinary boundary-polynomial
coefficients. The estimates also hold for finite-dimensional
spectators equipped with a submultiplicative norm.

For an invariant spectator \(A(z)\), the literal first-order
source identity is
\[
 \Lambda_\pm\bigl(g_m[V_{\pm,1}A-q^mw^m A]\bigr)
              =-\frac{\eta mN\rho}{2}A(c_0).
 \tag{20}
\]
This follows from (8),(15),(5): \(t(w_D)=-\rho\), and the
odd auxiliary idempotent vanishes there. Adding its inverted
identity gives the full archived even endpoint current. The
original factor \(\kappa^m\) is restored on both sides when
\(R^m\), rather than \(r_N^m\), is used.

## 5. Current-space size and the remaining source problem

For nonzero even \(m\), all shifts of \(m\delta p_D\) span
\(\delta\mathcal B_N\): the \(N\) vectors \(\delta p_j\)
have independent first jets. There is no vector space of
dimension independent of \(N\) containing this current and
closed under every lattice shift. It is a cyclic module under
\(U\); these statements are compatible.

The invariant radical has dimension \(\lfloor N/2\rfloor\).
At odd levels the pure normal at the fixed point is
anti-invariant and is absent from that radical. The two closing
extensions are two fixed types of functional, not a claim of
fixed vector dimension for every transported current.

The existing logarithmic-contour theorem already proves the
symmetrized shift identity and a polynomial bound for entire end
strips. Section 5 of the original coherent Gaussian note also
proves an affine first-order recurrence for the full filling
coefficient \(a(n)\), with its scalar endpoint term and complex-color
correction retained. That is a recurrence in the coefficient
label; (8)--(15) concern transport in the doubled spectral algebra
and the adjoint for an arbitrary spectator. The additional
construction here gives first-order
algebraic transport at both parities, identifies the failure of
the unmodified odd one-sided adjoint, and repairs it while
preserving the original closing on physical sources. It does not
identify arbitrary complex displacements with lattice shifts,
remove interpolation poles, or replace the geometric Newton
turn by \(U\).

Most importantly, (17)--(20) are relative to the actual spectator
norm. That norm may have an exponential rate larger than the
desired geometric contribution. These identities retain that
spectator and every current. They prove neither its gap nor a
nonzero coefficient after the original scalar closing.

## Direct written sources

The following full source versions were read for these
implications. No mathematical computation or test was used.

| Source | Direct implication | SHA256 |
|---|---|---|
| [Signed Gaussian Ward packet](research_signed_gaussian_ward_endpoint_packet.md) | Original crossing jets (7), both parities, and symmetric endpoint identity | 6bdced1b01917e41631386a24b337b60dfe5b04d35d70007cb56badc511a0191 |
| [Logarithmic contour transport](research_gaussian_logarithmic_contour_transport.md) | Double-cover normalization, original transported spectators, prior symmetric adjoints and whole-strip scope | e7d62f6630dec31ac6c87f75baf1ff707ed7af9221ac4c5199549cdd4ee7f36f |
| [Original dualizing residue](research_actual_source_dualizing_residue.md) | Full physical closing, double-node normals and odd simple-node normalization | 806f8e4530736632830a15cff19f4c0f72e659fa6280d48005c4184a6ffc9afb |
| [Original coherent Gaussian](actual_coherent_filling_gaussian_chirp.md) | Coverage comparison with the earlier full-coefficient recurrence in Section 5; no additional proof premise | d72f50bf1e9af5b15da89784c198a3cb5060b9ee9c3e6cc04b901049be516522 |

