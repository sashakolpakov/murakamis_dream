# Two source constants for the true bulk endpoint normal defect

Private written proof, 16 November 2026.

On a buffered physical-index interval, the true scalar normal defect
is intrinsic up to exponentially small errors among polynomially
bounded analytic value interpolants. Its exact discrete transport is
determined, to that accuracy, by two actual anchor coefficients.
The transport has an explicit two-dimensional continuum limit, regular
also at the coalescing parameter \(\alpha=0\).

No coefficient is set to zero or assumed small. This reduces the
compatibility question to two source constants; it does not answer
that question or estimate a filled source.

## 1. Source data and the true defect

Fix nested closed intervals
\[
 I_0\Subset\operatorname{int}I_1,\qquad
 I_1\Subset\operatorname{int}I_2,\qquad I_2\Subset(0,1/2),
                                                               \tag{1}
\]
and an anchor \(x_*\in\operatorname{int}I_0\). The notation means
positive distance from each indicated boundary. Let \(h=N^{-1}\),
\(x_j=j/N\), \(\theta=\pi/N\), and use the original data
\[
 c(r)=2\cos((2r+1)\theta),\quad c'(r)=-4\theta\sin((2r+1)\theta),
 \quad w_N(\alpha)=2\cosh(\alpha/N),
\]
\[
 F_j(\alpha)=K_N(c(j),w_N(\alpha)),\qquad
 G_j(\alpha)=\partial_zK_N(c(j),w_N(\alpha)).
                                                               \tag{2}
\]
Here \(K_N=\sum_{k=0}^{N-1}e_k\otimes e_k\) is the original Newton
kernel and the original physical relation is
\(P_N(z)=2T_N(z/2)+2\). Explicitly,
\(S_k=\prod_{r=1}^k2\sin(r\theta)\), \(S_0=1\), and
\(e_k(Z)=S_k^{-2}\prod_{r<k}(c(r)-Z)\).
All quantities are holomorphic in \(\alpha\).

An admissible value interpolation for this note is a function
\(f_N(x,\alpha)\), jointly holomorphic on a fixed complex neighborhood
of \(I_2\) and on a larger bounded complex parameter disk, such that
\[
 f_N(x_j,\alpha)=F_j(\alpha)\quad(x_j\in I_2),\qquad
                         \|f_N\|\le C N^p.                       \tag{3}
\]
The pinned two-channel theorem supplies one such family. Its separate
normal interpolation is not used to define the derivative in (3).
All statements below are uniform on a fixed smaller parameter disk.
Constants and strip widths may depend on the intervals, parameter
disks, and the bounds in (3), but not on \(N\).

Define the original value and common-index normal vectors
\[
 X_j=\binom{F_j}{N(F_j-F_{j-1})},\qquad
 Y_j=\binom{Nc'(j)G_j}
              {N^2[c'(j)G_j-c'(j-1)G_{j-1}]}.                    \tag{4}
\]
For the chosen scalar interpolation put
\[
 X_f(x)=\binom{f_N(x)}{N[f_N(x)-f_N(x-h)]},\qquad
                         D_j^f=Y_j-X_f'(x_j).                  \tag{5}
\]
The prime on \(X_f\) is in the normalized index \(x\). The first
component of \(D_j^f\) is exactly
\[
                      Nc'(j)G_j-\partial_xf_N(x_j).             \tag{6}
\]
Every node used in (4)--(5) lies inside \(I_2\) for large \(N\),
when \(x_j\in I_1\).

Use the original coefficients
\[
 A_N(r)=\frac{s_{r+1}^4}{s_{2r+1}s_{2r+2}},\qquad
 C_N(r)=\frac{s_r^4}{s_{2r}s_{2r+1}},\qquad s_r=2\sin(r\theta),
\]
\[
 q_N(x)=\frac{C_N(Nx)}{A_N(Nx)},\quad
 d_N(x)=\frac{c(0)-w_N(\alpha)}{A_N(Nx)},\qquad
 T_N(x)=\begin{pmatrix}1+d_N&q_N/N\\Nd_N&q_N\end{pmatrix}.
                                                               \tag{7}
\]
The full source equation and its common-index derivative give at
bulk physical nodes
\[
 X_{j+1}=T_N(x_j)X_j,\qquad
 Y_{j+1}=T_N(x_j)Y_j+T_N'(x_j)X_j.                               \tag{8}
\]
Their endpoint forcing vanishes to the required order at these
nodes only; it remains in the actual initial data (2), (4).

Let
\[
 E_f(x)=X_f(x+h)-T_N(x)X_f(x).
\]
The source adapter proves the exact identity
\[
               D_{j+1}^f=T_N(x_j)D_j^f-E_f'(x_j).               \tag{9}
\]
Thus it is the derivative of the scalar residual, not an arbitrarily
chosen homogeneous normal channel, that measures the forcing.

## 2. Intrinsic defect and exact discrete transport

**Theorem 1.** For all sufficiently large \(N\), the following hold
uniformly in the fixed parameter disk.

1. On a fixed complex neighborhood of \(I_1\), after shrinking its
   width if needed,
   \[
                   E_f,\ E_f'=O(N^P e^{-cN})                    \tag{10}
   \]
   for some \(P,c>0\).

2. If \(\widetilde f_N\) is any other family satisfying (3), then on
   \(I_1\)'s physical nodes
   \[
                   D_j^f-D_j^{\widetilde f}
                              =O(N^P e^{-cN}).                  \tag{11}
   \]
   Its constants may use the two common analytic neighborhoods and
   the larger of their polynomial bounds.

3. Choose a grid index \(j_*(N)\) nearest \(Nx_*\), and write
   \(x_{*,N}=j_*/N\) and \(\mathbf d_N^f=D_{j_*}^f\).
   Let \(\mathcal U_N(j,j_*)\) be the exact ordered product of the
   matrices \(T_N(x_r)\) from \(j_*\) to \(j\), using inverse products
   for \(j<j_*\). Then
   \[
    D_j^f=\mathcal U_N(j,j_*)\mathbf d_N^f
                                  +O(N^P e^{-cN}),\qquad x_j\in I_0,
                                                               \tag{12}
   \]
   \[
    \|\mathcal U_N(j,j_*)\|+
          \|\mathcal U_N(j,j_*)^{-1}\|\le C,\qquad
                            \|\mathbf d_N^f\|\le CN^P.           \tag{13}
   \]
   These are two actual source coefficients, intrinsic up to (11).
   They are not adjustable integration constants.

*Proof.* Cauchy estimates from (3) control all fixed derivatives on
smaller fixed domains. In particular
\[
 N[f_N(x)-f_N(x-h)]=\int_0^1f_N'(x-th)\,dt
\]
has the same polynomial bound there; so do \(X_f,E_f\) and their
fixed derivatives. At every interior physical node,
\(X_f(x_j)=X_j\), hence \(E_f(x_j)=0\) by (8).

We recall the precise dense-zero argument. A fixed disk about a real
point of \(I_1\), lying in the analytic neighborhood of \(I_2\), contains
at least \(c_1N\) grid nodes in a smaller central real interval. A
bounded holomorphic function with those zeros is bounded on a still
smaller disk by its original bound times \(q^{c_1N}\), \(q<1\):
divide by the associated disk Blaschke factors and apply the maximum
principle. The factor bound is uniform because both the zeros and
the smaller disk lie strictly inside the original disk. Cauchy's
formula on one more smaller disk gives the same exponential type
for fixed derivatives. Finitely many such disks cover \(I_1\), with
a common smaller strip. Applying this to \(E_f\) proves (10).

The same argument applied to \(f_N-\widetilde f_N\), which vanishes at
all nodes in \(I_2\), proves exponential bounds for this difference
and its first two derivatives on a buffered neighborhood of \(I_1\).
Equation (5), including its difference quotient, then gives (11).
No comparison with the ordinary off-grid kernel is made here.

The source theorem gives polynomial bounds for the actual \(F_j,G_j\)
on bounded complex parameter disks. Together with (3)--(5), this gives
the last assertion in (13). On a fixed neighborhood of \(I_1\),
\[
                   T_N=I_2+O(N^{-1}),\qquad
                   T_N^{-1}=I_2+O(N^{-1}),                       \tag{14}
\]
uniformly in the parameter. Multiplying \(O(N)\) such matrices along
the real buffered interval gives the first bounds in (13).
Variation of constants in (9) then bounds the error in (12) by
\(O(N)\) times (10) times these product bounds. Absorb that factor
into \(N^P\). Backward transport uses the same inverse bounds.
This proves the theorem. \(\square\)

Thus the unknown bulk defect is, to exponential precision, a
two-dimensional source datum. The theorem says nothing about the
size of that datum beyond its polynomial upper bound.

## 3. Explicit continuum modes and a uniform finite-step comparison

The first-order expansion of the exact transfer is
\[
 T_N(x)=I_2+\frac1N B(x,\alpha)+O(N^{-2}),
\]
\[
 B(x,\alpha)=
 \begin{pmatrix}
 0&1\\
 -(\pi^2+\alpha^2)\cot^2(\pi x)&
                  -\pi\{3\cot(\pi x)+\tan(\pi x)\}
 \end{pmatrix}.                                                   \tag{15}
\]
All fixed derivatives have the same uniform remainder on smaller
bulk domains. To verify it directly, the exact quotient in (7) is
\[
 q_N(x)=
 \left(\frac{\sin(\pi x)}{\sin(\pi x+\pi/N)}\right)^4
                \frac{\sin(2\pi x+2\pi/N)}{\sin(2\pi x)}.
\]
Hence
\[
 q_N(x)=1-\frac{\pi}{N}
                  \{3\cot(\pi x)+\tan(\pi x)\}+O(N^{-2}),
\]
where \(2\cot(2u)=\cot u-\tan u\). Also
\[
 A_N(Nx)=\tan^2(\pi x)+O(N^{-1}),\qquad
 c(0)-w_N(\alpha)=-(\pi^2+\alpha^2)N^{-2}+O(N^{-4}).
\]
Substitution in (7) proves (15).

Choose the holomorphic branch
\[
 \ell(x)=\log\sin(\pi x)
\]
that is real on the real bulk interval, shrinking its complex
neighborhood once if necessary. Put \(a_\alpha=\alpha/\pi\) and
\[
 f_0(x,\alpha)=\frac{\cos(a_\alpha\ell(x))}{\sin(\pi x)},\qquad
 f_1(x,\alpha)=\frac{\sin(a_\alpha\ell(x))}
                         {a_\alpha\sin(\pi x)}.                  \tag{16}
\]
The second expression uses its removable value
\[
 f_1(x,0)=\frac{\log\sin(\pi x)}{\sin(\pi x)}.
\]
These are entire in \(\alpha\), including at zero. Direct
differentiation shows that both solve
\[
 f''+\pi\{3\cot(\pi x)+\tan(\pi x)\}f'
                   +(\pi^2+\alpha^2)\cot^2(\pi x)f=0.             \tag{17}
\]
For \(\alpha\ne0\), equivalently use
\(\sin(\pi x)^{-1\pm i\alpha/\pi}\); (16) keeps the coalescence
at zero regular.

Define
\[
 \Phi(x,\alpha)=
 \begin{pmatrix}f_0&f_1\\ \partial_xf_0&\partial_xf_1\end{pmatrix}.
\]
Its Wronskian is exactly
\[
            \det\Phi(x,\alpha)
                  =\frac{\pi\cos(\pi x)}{\sin^3(\pi x)}.           \tag{18}
\]
Indeed the common factor is \(\sin(\pi x)^{-1}\), while the
Wronskian of \(\cos(a_\alpha\ell)\) and
\(\sin(a_\alpha\ell)/a_\alpha\) is \(\ell'\).
The determinant is independent of \(\alpha\) and is a unit on the
chosen bulk domain. Thus \(\Phi,\Phi^{-1}\) are uniformly bounded
on fixed compact parameter sets. They solve \(\Phi'=B\Phi\).

**Theorem 2.** Uniformly for \(x_j\in I_0\),
\[
 \mathcal U_N(j,j_*)=
       \Phi(x_j,\alpha)\Phi(x_{*,N},\alpha)^{-1}+O(N^{-1}).
                                                               \tag{19}
\]
Consequently, with the actual mode coefficients
\[
             \mathbf a_N^f(\alpha)
                        =\Phi(x_{*,N},\alpha)^{-1}\mathbf d_N^f,
\]
one has
\[
 \boxed{\quad
 D_j^f=\Phi(x_j,\alpha)\mathbf a_N^f(\alpha)
       +O\!\left(N^{-1}\|\mathbf a_N^f(\alpha)\|
                             +N^P e^{-cN}\right).
 \quad}                                                         \tag{20}
\]
All constants are uniform in the fixed complex parameter disk.
The coefficients are holomorphic in that parameter and independent
of the moderate value interpolant up to exponential errors.

*Proof.* Taylor's formula for the continuum fundamental matrix gives
\[
 \Phi(x+h)\Phi(x)^{-1}=I_2+hB(x,\alpha)+O(h^2).
\]
Its difference from \(T_N(x)\) is \(O(h^2)\) by (15). A telescoping
comparison of the two ordered products has \(O(N)\) terms, each
\(O(h^2)\), with their surrounding products uniformly bounded.
For the discrete products this is (13); for the continuum products
it follows from the bounded fundamental matrix and its inverse.
The result is \(O(Nh^2)=O(N^{-1})\). The same argument with inverses
works to the left of the anchor. Combining this with (12) proves
(20). Holomorphic parameter dependence follows from all exact
formulas; (11) and the bounded inverse in (18) prove its final
intrinsic assertion. \(\square\)

The error in (20) is relative to the norm of the two coefficients,
not to a potentially vanishing individual scalar component. At
\(\alpha=0\) the displayed logarithmic basis is required; no
division by \(\alpha\) is left.

## 4. Physical-parameter calibration and an exact cosh factor

There is actual source information about these two coefficients at
fixed imaginary parameters. Choose a fixed enlarged radius \(R_\alpha\)
whose boundary contains no zero of \(\cosh(\alpha/2)\), and construct
the admissible interpolation on a parameter disk strictly larger
than \(\{|\alpha|\le R_\alpha\}\). A desired bounded real interval
can be contained in a smaller disk \(|\alpha|\le A<R_\alpha\).

Every zero in the enlarged disk has the form
\[
             \zeta=\pm i(2b+1)\pi,\qquad b\ge0,                    \tag{21}
\]
and there are finitely many such zeros, independent of \(N\).
At this parameter, exactly
\[
                w_N(\zeta)=2\cos((2b+1)\pi/N)=c(b).
\]
For all sufficiently large \(N\), \(b\) is in the distinct physical
range. Since \(e_k(c(b))=0\) for \(k>b\), the ordinary kernel reduces
before any quotient to the degree-\(b\) polynomial
\[
 K_N(c(b),Z)=P_{b,N}(Z):=\sum_{k=0}^{b}e_k(c(b))e_k(Z).             \tag{22}
\]
The coefficients \(e_k(c(b))\) are \(O_b(1)\): the exact
difference-of-cosines product is
\[
              e_k(c(b))=\frac{S_{b+k}}{S_{b-k}S_k^2}.
\]
All indices in this expression are fixed, and cancellation of their
powers of \(N^{-1}\) gives that bound. On any fixed complex spectral
compact, \(e_k(Z)=O_b(N^{2k})\), directly from its \(k\) factors and
\(S_k^{-2}=O_b(N^{2k})\). Thus
\[
 p_{b,N}(x):=P_{b,N}(c(Nx))
\]
and all its fixed derivatives have polynomial bounds on a fixed
bulk neighborhood. This is an ordinary scalar value interpolation
with its actual compatible normal, not a selected solution of (17).

In fact at \(\alpha=\zeta\), ordinary differentiation of (22) gives
\[
 p_{b,N}'(x_j)=Nc'(j)G_j(\zeta),\qquad
                         X_{p_b}'(x_j)=Y_j(\zeta).                \tag{23}
\]
For the second component, the equality is explicitly
\[
 N[p_{b,N}'(x_j)-p_{b,N}'(x_j-h)]
       =N^2[c'(j)G_j(\zeta)-c'(j-1)G_{j-1}(\zeta)].
\]
Therefore its true two-component defect is exactly zero.
The difference \(f_N(\,\cdot\,,\zeta)-p_{b,N}\) has polynomial
analytic norm and vanishes at every physical node in \(I_2\).
The dense-zero argument in Theorem 1 controls its first two
derivatives exponentially on \(I_1\). Equations (5), (23), and the
bounded inverse of \(\Phi\) imply, for every zero (21),
\[
                       \mathbf a_N^f(\zeta)
                                 =O(N^P e^{-cN}).                \tag{24}
\]
The finitely many \(b\)'s permit common constants and exponent.

Here is an exact divisible version of this calibration. List all
the zeros inside \(|\alpha|<R_\alpha\) as \(\zeta_1,\ldots,\zeta_q\).
If there are none, use the empty correction. Otherwise let
\[
 L_\nu(\alpha)=\prod_{\mu\ne\nu}
                    \frac{\alpha-\zeta_\mu}{\zeta_\nu-\zeta_\mu},
 \qquad
 \mathbf r_N(\alpha)=\sum_{\nu=1}^{q}
                       \mathbf a_N^f(\zeta_\nu)L_\nu(\alpha).
                                                                    \tag{25}
\]
These are fixed-degree Lagrange polynomials. By (24),
\(\|\mathbf r_N\|_{|\alpha|\le R_\alpha}
 \le CN^Pe^{-cN}\). Every zero of \(\cosh(\alpha/2)\) in the disk
is simple, and the numerator in
\[
 \mathbf h_N(\alpha)=
       \frac{\mathbf a_N^f(\alpha)-\mathbf r_N(\alpha)}
                         {\cosh(\alpha/2)}                         \tag{26}
\]
vanishes at all of them. Thus all these apparent poles are removable.
There are no zeros on the disk boundary. The polynomial bound for
\(\mathbf a_N^f\), the positive minimum of
\(|\cosh(\alpha/2)|\) on that fixed boundary, and the maximum principle
give a polynomial bound for \(\mathbf h_N\) throughout the disk.
Consequently
\[
 \boxed{\quad
 \mathbf a_N^f(\alpha)=\cosh(\alpha/2)\mathbf h_N(\alpha)
                                      +\mathbf r_N(\alpha),\qquad
 \|\mathbf h_N\|\le CN^P,\quad
 \|\mathbf r_N\|\le CN^Pe^{-cN}.
 \quad}                                                         \tag{27}
\]
The equality is exact; only the bound on its correction is
asymptotic. Fixed parameter derivatives retain the same estimates
on smaller disks by Cauchy's formula.

This calibration uses genuine low-degree physical kernels at every
zero (21). It does not infer a factor by analytic continuation from
finitely many approximate zeros without a correction: (25) is that
correction. On the real parameter axis \(\cosh(\alpha/2)\) never
vanishes. The quotient \(\mathbf h_N\) remains unknown, so (27)
does not establish nonvanishing, smallness, or a leading coefficient
for real microscopic endpoint parameters.

## 5. Exact criterion for a moderate scalar Hermite representative

The two coefficients characterize, rather than merely accompany,
the missing local scalar interpolation. All intervals in this
statement retain fixed buffers about the anchor; a smaller fixed
strip is allowed. Exponential estimates may include a polynomial
factor in \(N\).

**Corollary 3.** The following are equivalent:

* The actual anchor vector \(\mathbf a_N^f\) is exponentially small.
* On a fixed smaller bulk interval containing the anchor there is
  a polynomially bounded holomorphic scalar \(h_N(x,\alpha)\)
  matching both physical channels:
  \[
  h_N(x_j,\alpha)=F_j(\alpha),\qquad
            \partial_xh_N(x_j,\alpha)=Nc'(j)G_j(\alpha).
                                                               \tag{28}
  \]

For the forward implication, (28) can be imposed at every node of
\(I_0\). For the converse it suffices to have (28) on any fixed
neighborhood of the anchor, with an analytic strip and a polynomial
bound there. Uniformity in a fixed parameter set is retained when
the hypotheses are uniform on a larger parameter neighborhood.
The condition is independent of the chosen admissible \(f_N\) in
the exponential sense of (11).

*Proof of necessity.* On the given neighborhood,
\(h_N-f_N\) is polynomially bounded, holomorphic, and zero at every
physical value node. Dense zeros therefore make its derivatives
exponentially small near the anchor. By (28),
\(X_h'(x_j)=Y_j\), including the second component formed from the
preceding node. Consequently
\[
 \mathbf d_N^f
       =X_h'(x_{*,N})-X_f'(x_{*,N})
                                  =O(N^P e^{-cN}).
 \]
Multiplication by the bounded inverse of \(\Phi\) proves the first
condition. The finite difference in component two costs at most a
polynomial factor, or may be bounded by the second derivative.

*Proof of sufficiency.* Exact transport (12), not just the
continuum approximation, makes all \(D_j^f\) exponentially small
for \(x_j\in I_0\). Let \(\Delta_j\) denote their first components.
On a fixed smaller strip define the finite correction
\[
 h_N(x,\alpha)=f_N(x,\alpha)+
   \sum_{j:\,x_j\in I_0}
       \Delta_j(\alpha)(x-x_j)\operatorname{sinc}^2(Nx-j),
 \qquad \operatorname{sinc}z=\frac{\sin\pi z}{\pi z}.
                                                               \tag{29}
 \]
At its own node, each summand has value zero and derivative
\(\Delta_j\). At every other grid node its sinc square has a double
zero. Thus (29) gives both equalities (28) exactly.

There are \(O(N)\) nodes, \(|x-x_j|\) is uniformly bounded on the
fixed strip, and
\[
 |\operatorname{sinc}^2(Nx-j)|\le e^{2\pi N|\Im x|}.
 \]
If \(|\Delta_j|\le CN^P e^{-cN}\), the correction is at most
\[
             CN^{P+1}e^{-cN+2\pi N|\Im x|}.
 \]
Choose a fixed strip height less than \(c/(4\pi)\), also inside the
analytic domain of \(f_N\). The correction is exponentially small
there, and \(h_N\) has polynomial norm. Holomorphic parameter
dependence and fixed derivative bounds follow directly and by
Cauchy on smaller domains. This proves sufficiency. \(\square\)

On a sufficiently narrow bulk strip the map
\(x\mapsto c(Nx)=2\cos(2\pi x+\pi/N)\) is one-to-one with nonzero
derivative. Indeed the two possibilities for equality of cosines
require either \(x-y\in\mathbb Z\) or
\(x+y+1/N\in\mathbb Z\). The first gives \(x=y\) in this
rectangle; the second is impossible because its real part lies
strictly between zero and one for large \(N\).
Its local inverse converts (28) to an actual
scalar spectral Hermite representative there.

This equivalence does not prove its smallness premise for real
\(\alpha\). It supplies no full-period representative or endpoint
extension, and no boundary current has been discarded.

## 6. Scope and direct sources

The first component of this transported defect is the actual missing
spectral normal, multiplied by \(Nc'(j)\). Its contribution to the
original trace is the exact current in the pinned normal-defect
source, with the original crossing, remaining spectator, shared
colors, and all other traces retained. A polynomial upper bound for
the two coefficients is not a filled-action bound for that current.

Neither transport theorem says that \(\mathbf a_N^f\) is nonzero,
zero, exponentially small, or of a specified algebraic order at
real parameters. Section 4 gives only its physical-parameter
calibration and divisible correction. Establishing its actual real
leading coefficients remains a separate source calculation.
The common-index determinant's homogeneous remainder is not
substituted for the true defect (5).

The endpoints of the physical interval, all external connectors,
the odd simple node, and the full-period interface are outside this
buffered bulk transport. A scalar moderate Hermite representative
follows only under the equivalent smallness condition of Corollary 3.
No completed contour follows merely from the two-mode reduction.

A coverage search of the endpoint and physical-row notes found the
exact prolonged recurrence and the true residual adapter, but not
this intrinsic two-constant reduction with explicit Euler comparison.
Both complete direct source proofs were read at the following
unchanged versions, and their used implications and hashes checked:

* [True endpoint normal defect and bulk primitive](research_endpoint_normal_defect_bulk_primitive.md),
  SHA256 60abb9d3e569fae7cd088a752d5f07211a1eeb444ffbd494b376470074ccfec7:
  true defect, its exact residual recurrence, the retained trace
  current, and the distinction from the common-index initial channel.
* [Moderate two-channel bulk interpolation](research_microscopic_endpoint_two_channel_interpolation.md),
  SHA256 44f6db0f8afdf1205ab8b0935b95b8a4fd9fa16c6414be2467b8b40a123c0ffe:
  actual prolonged transfer, polynomial initialization, the analytic
  value interpolant, and the quantitative dense-zero proof.

Only written mathematics, source-text reads, and file hashes were
used. No mathematical program, numerical experiment, test, or build
was run. Adopted notes and public manuscripts remain unchanged.

