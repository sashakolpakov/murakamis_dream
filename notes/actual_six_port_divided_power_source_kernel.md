# The actual six-port source is an explicit divided-power kernel

29 October 2026. The saturated specialization of GENERIC invariant tensors
inside the full root-level six-head invariant space has an explicit
single divided-power equation. The equation is surjective onto a specified
physical degree space. Its right inverse and an algebraic source projection
are given below at every \(N\), including even and composite levels.
This does not assume a semisimple root tensor category or a tame recoupling
frame.

## 1. Regular actual divided operators on any fixed number of heads

Put \(d=N-1,\ q=e^{\pi i/N},\ Q=q^2,\ \rho=q-q^{-1}\).
The actual generic highest-weight \(N\)-head, in the balanced analytic
basis, is

\[
 F|a\rangle=(1-\zeta^{2a+2})|a+1\rangle,\quad
 \mathcal E|a\rangle=(\zeta^{-N}-\zeta^{N-2a})|a-1\rangle,\quad
 K|a\rangle=\zeta^{d-2a}|a\rangle.                       \tag{1}
\]

Outside-basis arrows vanish. Set \(E=\mathcal E/(\zeta-\zeta^{-1})^2\).
Direct adjacent entries give
\([E,F]=(K-K^{-1})/(\zeta-\zeta^{-1})\).
For an ordered \(r\)-head block use the original coproducts

\[
 \mathcal E_r=\sum_i\mathcal E_i\prod_{j>i}K_j,\qquad
 F_r=\sum_i\prod_{j<i}K_j^{-1}F_i.                       \tag{2}
\]

For \(n\leq N\), their divided powers are REGULAR at \(\zeta=q\):

\[
 \mathcal E_r^{[n]}=\mathcal E_r^n/[n]_\zeta!,\qquad
 F_r^{[n]}=F_r^n/[n]_\zeta!.
\]

Here division is made in the specified generic family before
specialization. To prove regularity without dividing a zero root matrix,
normal order the \(Q\)-commuting summands of (2). With
\(s_i=\sum_{j<i}n_j,\ t_i=\sum_{j>i}n_j,\ C=\sum_{i<j}n_in_j\), one obtains

\[
 \mathcal E_r^{[n]}
 =\sum_{\sum n_i=n}\zeta^C\bigotimes_i
                         \left(\mathcal E_i^{[n_i]}K_i^{s_i}\right),
\quad
 F_r^{[n]}
 =\sum_{\sum n_i=n}\zeta^{-C}\bigotimes_i
                         \left(K_i^{-t_i}F_i^{[n_i]}\right). \tag{3}
\]

This follows directly from the finite Gaussian binomial expansion, and
then induction in the number of tensor factors. Terms with a local
\(n_i=N\) are identically zero because the single head has dimension
\(N\). Every other local denominator in (3) is a unit at the root.
Thus (3) is also an explicit all-entry formula, with all original
Cartan phases and no choice of a root divided by zero.

Define the equivalent first-normal operators

\[
 J_{\mathcal E,r}=\left[\frac{\mathcal E_r^N}{1-\zeta^{2N}}\right]_q,
 \qquad
 J_{F,r}=\left[\frac{F_r^N}{1-\zeta^{2N}}\right]_q.          \tag{4}
\]

They equal their divided operators times the same nonzero scalar

\[
 \alpha_N=
 \left[\frac{[N]_\zeta!}{1-\zeta^{2N}}\right]_q
 =\frac{Nq^{-N(N-1)/2}}{(1-Q)^N}.                         \tag{5}
\]

They lower or raise integer degree by exactly \(N\).
Every actual adjacent \(R^{\pm1}\) commutes with these total operators:
the literal finite generic \(R\) intertwines (2), hence their powers,
and scalar division followed by regular specialization proves the claim.
This keeps the full original crossing, not its eigenvalue-only quotient.

## 2. An elementary divided commutation calculation

For the standard \(E=\mathcal E/(\zeta-\zeta^{-1})^2\), a vector of weight
\(H\) satisfies the generic finite identity

\[
 E^{[a]}F^{[b]}v_H
   =\sum_{t=0}^{\min(a,b)}
       {H+a-b\brack t}_\zeta
                   F^{[b-t]}E^{[a-t]}v_H.                \tag{6}
\]

Negative upper Gaussian indices, when needed, are interpreted by their
finite product. A direct proof starts with

\[
 EF^{[b]}=F^{[b]}E+
    F^{[b-1]}\frac{\zeta^{1-b}K-\zeta^{b-1}K^{-1}}
                         {\zeta-\zeta^{-1}} .
\]

This is the sum of \(b\) elementary commutators; the geometric sum is
\([b]_\zeta\). Repeating it \(a\) times, dividing by \([a]_\zeta!\), and
grouping equal \(F^{b-t}E^{a-t}\) terms gives (6) by the Gaussian
Pascal recursion. Equivalently its Cartan coefficient is
\({K;2t-a-b\brack t}\). Acting AFTER \(E^{[a-t]}\) turns its upper
integer into \(H+a-b\), which explains the weight in (6).
This is a polynomial/rational identity derived from (1), not an
assumption about root-module decomposition.

Now consider FOUR physical heads and the two specified degree spaces

\[
 W=(V_N^{\otimes4})_{2N-2},\qquad
 L=(V_N^{\otimes4})_{N-2}.                                \tag{7}
\]

Vectors of \(L\) have weight \(H=2N\). For \(a=b=N\), all matrices in
(6) have the regular specialization (3). The root Gaussians obey

\[
 {2N\brack t}_{q}=0\quad(0<t<N),\qquad
 {2N\brack N}_{q}=2(-1)^N.                               \tag{8}
\]

For a direct proof use
\(\prod_{j=0}^{2N-1}(1+Q^jz)=(1-(-z)^N)^2\) and compare coefficients;
the symmetric Gaussian has the additional phase
\(q^{-t(2N-t)}\). Also \(E_4^{[N]}L=0\), simply because its output
degree would be negative. Thus (6)--(8) give the exact RIGHT INVERSE

\[
 \boxed{\quad
 \mathcal E_4^{[N]}F_4^{[N]}|_L
                 =2(-1)^N\rho^{2N}I_L,\qquad
 J_{\mathcal E,4}J_{F,4}|_L=-2N^2I_L .
 \quad}                                                  \tag{9}
\]

For the second equality use (5),
\(1-Q=-q\rho,\ q^{-N(N-1)}=(-1)^{N-1}\).
Both signs in (9) include even levels. In particular
\(J_{\mathcal E,4}:W\to L\) is surjective, with explicit right inverse
\(-J_{F,4}/(2N^2)\).

## 3. Original six-head invariants and extraction of this constraint

The [complete original source construction](actual_complete_source_multiplicity_module.md),
section 5, gives an isomorphism between the FULL root invariant space
in six heads WITH unrolled \(H=0\) and \(W\). Throughout this note
\(\operatorname{Inv}_{\mathrm{root}}\) includes this \(H=0\) condition, not
only the periodic equation \(K=1\). Write its map as \(\Phi\). Explicitly,

\[
 H_2(w)=\sum_{c=0}^d\frac{(-xQ)^c}{(Q;Q)_c}
                    \mathcal E_4^cw\otimes|c\rangle,\qquad
 \Phi_w=N\sum_{a=0}^d
       \frac{x^{a-d}}{(Q;Q)_a}F_5^aH_2(w)\otimes|d-a\rangle .
                                                               \tag{10}
\]

Its inverse \(\mathsf{ext}\) extracts last two colors \((0,d)\)
and multiplies by \(x^d/N\), where \(x=q^d\).
Using (3) on (10) yields

\[
 \boxed{\qquad
 \mathsf{ext}\bigl(J_{\mathcal E,6}\Phi_w\bigr)
                         =J_{\mathcal E,4}w .\qquad}       \tag{11}
\]

Here the extraction is also defined on the shifted output degree.
The details prevent a false deletion of endpoint terms: output last
color \(d\) forces \(a=0\) and local lowering on head six equal to zero.
For fifth input color \(c\), its local divided exponent must equal
\(c\). If \(c>0\), the first-four-head factor contains
\(\mathcal E_4^{[N-c]}\mathcal E_4^c
 =\mathcal E_4^N/[N-c]_q!=0\) at the root; its denominator is a unit.
For \(c=0\), it is the FULL divided operator
\(\mathcal E_4^{[N]}\). The remaining two Cartan factors multiply to
\(K_5^NK_6^N=1\), and the original \(Nx^{-d}\) cancels the extraction
factor. Multiplication by the common scalar (5) proves (11).

## 4. Equality with saturated generic source, at all levels

Let \(\mathcal O=\mathbb C\{\zeta-q\}\) and \(\mathcal K=\operatorname{Frac}\mathcal O\).
Inside the free balanced six-head lattice take

\[
 \Lambda=\operatorname{Inv}_{\mathcal K}(V_d(\zeta)^{\otimes6})
                     \cap\mathcal O^{N^6},\qquad
 S_N=\Lambda/(\zeta-q)\Lambda.
\]

The [generic-source saturation proof](actual_six_port_deformable_source_and_recoupling.md)
shows that \(S_N\) injects into the full root invariants, with dimension
\((N^3+N)/2\). Saturation matters: \(\Lambda\) is a free direct summand
over this DVR, so reduction is injective. It is not the kernel obtained
by substituting the root into a generic rank formula.

Every vector in \(\Lambda\) is annihilated by the generic ordinary
\(E_6,F_6\), hence by the regular divided operators (3). Therefore
\(S_N\subset\ker J_{\mathcal E,6}\cap\ker J_{F,6}\).
By (11), \(\mathsf{ext}(S_N)\subset\ker J_{\mathcal E,4}\).
The actual dimensions and (9) are

\[
 \dim W=\frac{2N^3+N}{3},\qquad
 \dim L={N+1\choose3},\qquad
 \dim\ker J_{\mathcal E,4}=\frac{N^3+N}{2}.
\]

The first is the central coefficient of \((1+z+\cdots+z^d)^4\);
the second counts the unconstrained compositions of \(N-2\) into
four parts. The last now follows from PROVED surjectivity, not
assumed flatness. Equal dimensions give the all-level identification

\[
 \boxed{\quad
 \mathsf{ext}(S_N)=\ker(J_{\mathcal E,4}:W\to L),\qquad
 S_N=\operatorname{Inv}_{\mathrm{root}}\cap\ker J_{\mathcal E,6}
    =\operatorname{Inv}_{\mathrm{root}}\cap
                         \ker J_{\mathcal E,6}\cap\ker J_{F,6}.
 \quad}                                                  \tag{12}
\]

Thus the extra \({N+1\choose3}\) root invariants are precisely the
divided-current obstruction. No tilting decomposition, classical
semisimplicity, or numerical braid-cyclic rank was used for equality.

## 5. Explicit source projection and its exact scope

On \(W\), define

\[
 \boxed{\qquad
 \mathsf P=I_W+\frac{J_{F,4}J_{\mathcal E,4}}{2N^2}.
 \qquad}                                                 \tag{13}
\]

By (9), \(\mathsf P^2=\mathsf P\), \(J_{\mathcal E,4}\mathsf P=0\),
and its range is exactly the source space (12). The complement is
\(\operatorname{im}J_{F,4}\), and its rank is \({N+1\choose3}\).
This is an explicit SOURCE-INDEPENDENT algebraic projection defined
by known tensor generators; it is not evaluation at an unknown invariant.
It is generally oblique, and no polynomial bound on its norm is claimed.
The orthogonal projection onto the same known kernel has norm one.

The original three-cup source lies in \(S_N\). This follows either from
its regular generic lift or directly: every nontrivial local divided
power on a two-head cup is zero (ordinary powers by its Hopf equations,
and the \(N\)-th powers by physical degree). The block coproduct (3)
then kills the three-cup tensor. Every literal signed braid preserves
\(S_N\) by its regular generic intertwining. Any polynomial interval
Casimir coupon has the same property. A complete circle has such a
regular polynomial lift; no actual generic-\(q\) pivot germ is replaced
when using this statement AT THE FIXED ROOT.

Consequently \(\mathsf P\) can be inserted between reduced gates on an
original source orbit without changing any original exterior co-source.
It need not commute with every reduced boundary generator on the
UNRESTRICTED root space. An arbitrary root-only intertwiner without a
regular generic lift is not asserted to preserve \(S_N\).

All genuine original Casimir Hermite derivatives remain in the
restricted braid/coupon operators. Restriction (12) removes root
invariants absent from the generic source; it is not a semisimplification
or an instruction to set their normal currents to zero. A derivative
of the whole source in \(q\) satisfies an INHOMOGENEOUS differentiated
Ward equation; (12) is a root-value theorem and does not replace that
equation by a homogeneous one.

For the six-head original plat, \(w_0=p\otimes p\) and
\(\lambda=\ell\otimes\ell\) in \(W\). The literal marked cap is evaluated
only after the whole invariant identification (10); it gives this
\(\lambda\), as already proved in the complete-source note. Physical
orthogonal compression to (12) therefore preserves the word scalar
and keeps the boundary Cauchy cost at most
\(\|w_0\|\|\lambda\|=N^2\). No new boundary normalization is inserted.

This supplies a concrete smaller six-port source for subsequent
recoupling and energy estimates. It does not yet prove a positive
geometric norm bound or a new noncyclic volume-equality class.

Audit: [literal divided coproduct, right inverse, source and braid matrices](../experiments/audit_actual_six_port_divided_power_source_kernel.py).
