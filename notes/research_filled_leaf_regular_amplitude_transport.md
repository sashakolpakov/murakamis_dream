# Regular amplitude transport for the actual terminal slow block

Private written proof, 16 November 2026.

The actual terminal operator has an additional cancellation not
shared by a generic perturbation of a double characteristic.
After a scalar gauge its midpoint coefficients are even in the
level spacing. This removes the first-order error on a constant
WKB amplitude. The full endpoint-product forcing starts at second
order, so the actual slow block admits a polynomially conditioned
gauge with transfer \(I+hB_h\), where \(B_h\) is bounded.
Both original value and independent normal channels are retained.

The result concerns fixed bulk intervals. It improves the
subexponential cost of slow transport to a polynomial cost; it
does not initialize a nonzero slow packet or estimate its original
scalar closing.

## 1. Actual source and the statement

Use the original algebra, turn and crossing
\[
 {\cal A}_N=\mathbb C[Z]/(P_N),\quad
 P_N(Z)=2T_N(Z/2)+2,\quad q=e^{\pi i/N},\quad
 c_0=q+q^{-1},\quad C f=Zf\pmod {P_N},
\]
\[
 J=TCT,\qquad V_n=\kappa^nTR^{-n}T,\qquad
 D_n=V_nCV_{-n},\qquad \kappa=q^{(N-1)^2/2}.
 \tag{1}
\]
Here \(T_N\) is Chebyshev's polynomial. Fix an integer
\(|n|\ge2\), a fixed number \(r\ge1\) of endpoint factors, and
a bounded complex parameter polydisk. The literal leaf is
\[
 F_N=T(R^nB_N),\qquad
 B_N=\operatorname{can}\prod_{i=1}^r
                  K_N(2\cosh(\alpha_i/N),Z).
 \tag{2}
\]
The empty product can be padded by \(K_N(c_0,Z)=1\), with
\(\alpha=i\pi\). All products in (2) and all their normals
are in the original full algebra.

Put \(h=N^{-1}\), \(u_j=jh\), and use the centered coordinate
\[
 x=u+h/2,\qquad c(x)=2\cos(2\pi x),\qquad
 {\cal S}(x)=S_n(\pi-2\pi x).
 \tag{3}
\]
The phase is precisely the signed phase of the jet-adjoint
source, including its additive constant. Thus its former
\({\cal S}_h(u)\) equals \({\cal S}(x)\). The signed root
identity is
\[
 e^{{\cal S}'(x)}=\tau_{\max,-n}(x).
 \tag{4}
\]
This is the root of the actual \(D_{-n}\) equation, and is
uniquely largest in modulus on the real physical bulk.

Fix a closed interval inside \((0,1/2)\), with several fixed
larger buffers still inside \((0,1/2)\). All holomorphic
domains below are sufficiently thin fixed complex tubes over
these buffers. Constants may depend on the buffers, \(n,r\)
and the parameter polydisk, but not on \(N\).

**Theorem.** On a smaller fixed tube the actual normalized
slow dynamics has dimension \(4\,6^r\). It has a holomorphic
frame and inverse on its image costing at most a fixed power
of \(h^{-1}\), in which its transfer is
\[
                         {\cal T}_h(x)=I+h{\cal B}_h(x),
 \qquad \|{\cal B}_h\|\le C .
 \tag{5}
\]
Every fixed derivative is bounded on smaller tubes. The
embedding has an invariance residual at most
\(Ce^{-c_*/h}\), for some \(c_*>0\), also after fixed derivatives. The dimension
counts both independent physical value and normal copies;
neither copy is discarded.

In these coordinates the forward and inverse propagators
across a fixed bulk interval are bounded by a constant.
In the original normalized slow-packet norm both cost at
most \(Ch^{-p}\), for some fixed \(p\).

More explicitly, let \(X_j\) be the whole base-phase-normalized
actual packet of the jet-adjoint source and let
\({\cal B}_N^*=1+\max\|X_j\|=e^{o(N)}\) on a larger real
buffer, uniformly in the parameters. After any fixed positive
left buffer, for any two rows \(j,l\) in the remaining interval,
\[
 \boxed{\quad
 \|X_j\|\le Ch^{-p}\|X_l\|
                 +e^{-c_1/h}{\cal B}_N^*,
 \qquad
 \|X_l\|\le Ch^{-p}\|X_j\|
                 +e^{-c_1/h}{\cal B}_N^* .
 \quad}
 \tag{6}
\]
The constants in (6) also depend on that positive left buffer.
This is an additive-error comparison of actual packet norms.
It gives no lower bound when the actual slow projection is
unknown, and a packet norm is not the original trace.

## 2. Lifting the symmetric operator identity

The ordinary physical-row lift in the terminal transfer source
has finite shifts and rational coefficients in
\(v=e^{2\pi ix}\) and \(q\). For each fixed signed index its
shift order and rational degrees are bounded independently
of \(N\). Both exact algebra recurrences are
\[
 qD_{a+2}+q^{-1}D_a+D_{a+1}J=8I,\qquad
 q^{-1}D_{a+2}+qD_a+JD_{a+1}=8I .
 \tag{7}
\]
We need both identities for the ordinary difference lift,
not just their classes modulo \(P_N\).

Here is a finite argument for this lift. Take the difference
between either side of (7), using the ordinary lifts, and
write it as \(\sum_{|k|\le b}r_{k,N}(v)E^k\), where
\(E f(x)=f(x+h)\). The integer \(b\), the rational degrees,
and the number of excluded denominator zeros are fixed.
At a regular physical row well away from the two endpoints,
the \(2b+1\) shifted spectral colors are distinct. For all
large \(N\), an ordinary polynomial of degree at most \(2b\),
hence less than \(N\), can prescribe arbitrary values at these
colors. The finite-algebra identity says the difference
vanishes on every such polynomial at that physical row.
Therefore every \(r_{k,N}\) vanishes there.

There are a number proportional to \(N\) of these rows.
After clearing its fixed-degree rational denominator, each
coefficient is a Laurent polynomial in \(v\) of fixed degree.
For sufficiently large \(N\), its distinct physical zeros
force it to be identically zero. Thus (7) holds as an
ordinary difference identity at every sufficiently large
actual level. The coefficients are meromorphic in \(q\)
near \(1\), with at worst fixed-order poles. Multiplying
by a fixed power of \(q-1\) and using the infinitely many
levels accumulating at \(q=1\) proves the same identity
of coefficient germs there.

This argument does not turn the source's ordinary residual
into zero off the grid. It lifts an operator identity, using
arbitrary test polynomials; the source equations still have
their original \(P_N\)-multiple residuals.

Adding (7) now gives the exact ordinary identity
\[
 \boxed{\quad
 \widetilde D_{a+2}
   ={16\over c_0}I-\widetilde D_a
     -{\widetilde D_{a+1}\widetilde J+
                       \widetilde J\widetilde D_{a+1}\over c_0}.
 \quad}
 \tag{8}
\]
Its use is local near \(h=0\), where \(c_0\) is a unit.
No assertion at the exceptional \(N=2\) denominator is needed.

## 3. Exact even midpoint coefficients

Choose the holomorphic square root positive on the real bulk,
and put
\[
 p(x)=(\sin 2\pi x)^{-1/2},\qquad a(x)=\tan^2(\pi x).
 \tag{9}
\]
The two ordinary coefficients of \(J\), in the centered
coordinate, are
\[
 A(x,h)=a(x+h/2){\sin2\pi(x+h/2)\over\sin2\pi x},
 \qquad
 C(x,h)=a(x-h/2){\sin2\pi(x-h/2)\over\sin2\pi x}.
 \tag{10}
\]
Thus \(\widetilde J=c_0+A+C-AE-CE^{-1}\).
After conjugating by \(p\), the forward coefficient at its
midpoint \(z=x+h/2\) is minus
\[
 b(z,h)=
 {a(z)\sin2\pi z\over
  \sqrt{\sin2\pi(z-h/2)\sin2\pi(z+h/2)}}.
 \tag{11}
\]
The backward midpoint coefficient is likewise \(-b(z,h)\).
The function \(b\) is exactly even in \(h\).
The diagonal \(c_0+A+C\) is even in \(h\) at fixed \(x\).

The physical formula for \(\widetilde D_\sigma\) has forward
coefficient \(A(x,h)e^{-2\pi i\sigma(x+h/2)}\), backward
coefficient \(C(x,h)e^{2\pi i\sigma(x-h/2)}\), and diagonal
\[
                  {8-c(x)(c_0+A+C)\over c_0}.
 \tag{12}
\]
Consequently \(p^{-1}\widetilde D_\sigma p\) has the even
midpoint coefficients \(b(z,h)e^{-2\pi i\sigma z}\) and
\(b(z,h)e^{2\pi i\sigma z}\), and an even diagonal.
Ordinary multiplication by \(c(x)\) is also even.

For precision, the Weyl symbol here simply means the finite sum
\[
 {\mathsf a}(x,\xi,h)=\sum_k a_k(x,h)e^{k\xi}
 \quad\hbox{for}\quad
 {\mathsf A}=\sum_k a_k(x+kh/2,h)E^k .
 \tag{13}
\]
No pseudodifferential theorem is being invoked. If two scalar
operators have even midpoint coefficients, so does their
anticommutator. Indeed the coefficient of the product shifts
\(k+l\), at their common midpoint \(z\), is
\[
             a_k(z-lh/2,h)b_l(z+kh/2,h).
 \tag{14}
\]
Replacing \(h\) by \(-h\) exchanges this with the reversed
product coefficient. Summing the two proves the assertion.

Starting from \(D_0=C,D_1\), and separately from \(D_0,D_{-1}\),
identity (8) therefore proves:
\[
 \boxed{\quad
 p^{-1}\widetilde D_a p
 \text{ has exactly even midpoint coefficients for every fixed }
 a\in\mathbb Z .
 \quad}
 \tag{15}
\]
In particular its Weyl subprincipal coefficient vanishes.
The assertion concerns the original ordered quantum operator,
not just the even expansion \(c_0=2+O(h^2)\).

## 4. The actual second-order constant-amplitude residual

Let \({\mathsf P}_h=p^{-1}(\widetilde D_{-n}-c_0)p\), and
write its leading Weyl symbol as \(P_0(x,\xi)\). By the signed
terminal classification and (4),
\[
 P_0(x,{\cal S}'(x))=0,\qquad
 \partial_\xi P_0(x,{\cal S}'(x))=0 .
 \tag{16}
\]
The root is exactly double and separated on the fixed tube.
For each finite shift, direct Taylor expansion gives
\[
 { {\mathsf P}_h e^{{\cal S}/h}\over e^{{\cal S}/h}}
 =P_0(x,{\cal S}')
  +{h\over2}
       \{\partial_x\partial_\xi P_0
                  +{\cal S}''\partial_\xi^2P_0\}
                         (x,{\cal S}')+O_{\rm hol}(h^2).
 \tag{17}
\]
There is no first-order midpoint-symbol term by (15).
The expression in braces is
\(d_x[\partial_\xi P_0(x,{\cal S}'(x))]\), hence is zero.
All remainders and fixed derivatives are uniform on smaller
fixed tubes. Therefore the literal scalar test amplitude
\[
                        f_h(x)=p(x)e^{{\cal S}(x)/h}
 \tag{18}
\]
satisfies
\[
                 f_h^{-1}(\widetilde D_{-n}-c_0)f_h
                                      =O_{\rm hol}(h^2).
 \tag{19}
\]
The left side of (19) denotes application to the constant
amplitude \(1\), not an operator-norm estimate.

Now use all the actual gauged input channels from the leaf
source. Write \(d=6^r\), \(k=33r\). Their exact equation and
product recovery are
\[
 \{d_h(J)(D_{-n}-c_0)I_d-s^2E_h(J)\}{\cal F}_N=0,
 \qquad
 (J-2)^rF_N={\cal F}_{N,*},\qquad s=q-q^{-1}.
 \tag{20}
\]
The scalar polynomial \(d_h\) and the matrix polynomial \(E_h\)
have fixed degree and bounded holomorphic coefficients;
\(d_h(Z)\to(Z-2)^k\). The order in (20) is essential.

Conjugation of any fixed finite shift by \(f_h\) has bounded
holomorphic coefficients on these tubes, since
\(({\cal S}(x+\ell h)-{\cal S}(x))/h\) is bounded there.
Consequently (19), the left placement of \(d_h(J)\), and
\(s^2=O(h^2)\) show that the whole first operator in (20),
after this conjugation, applied to any constant vector
in \(\mathbb C^d\), is \(O_{\rm hol}(h^2)\).
This includes the actual source-coupling matrix \(E_h\).

Only grid values and first normals of (20) are used.
Its ordinary residuals remain multiples of \(P_N\);
their values and first derivatives vanish at the physical
double nodes. Multiplication by the nonzero local \(f_h\)
does not change that fact.

## 5. Fixed slow columns and the polynomial gauge

Use the companion of the first equation of (20), after
normalizing each shifted entry by its own \(f_h\). Denote it
by \(M_h(x)\), with \(2(k+|n|)\) positions per channel.
Its leading extreme coefficient is a unit on the tube.
Equation (19) and the conclusion after (20) say
\[
                   M_h{\bf r}={\bf r}+O_{\rm hol}(h^2),
 \tag{21}
\]
where \({\bf r}\) inserts a constant vector at every position.
Let \({\bf v}\) insert the same vector times the integer
position offset. The double-root companion identity gives
\[
 M_0{\bf r}={\bf r},\qquad M_0{\bf v}={\bf v}+{\bf r}.
 \tag{22}
\]
Both columns are constant in \(x\). The other principal
roots are strictly stable after normalization by (4).
There are \(d\) copies of the pair (22).

Choose a holomorphic stable complement by the Riesz/Kato
construction of the slow-graph source. Its slow columns
can be exactly \({\bf r},{\bf v}\): the Riesz projection
has constant range spanned by these columns, and its
derivative annihilates both. The Kato equation therefore
fixes them. In this frame, evaluated at both ends of the step,
\[
 \widetilde M_h=
 \begin{pmatrix}A_h&B_h\\ C_h&D_h\end{pmatrix},\quad
 A_0=\begin{pmatrix}I_d&I_d\\0&I_d\end{pmatrix},\quad
 B_h,C_h=O(h),\quad D_h=D_0+O(h).
 \tag{23}
\]
Here \(D_0\) is strictly stable. If \(e\) denotes the first
\(d\) slow columns, (21) gives the stronger identities
\[
                 (A_h-I)e=O(h^2),\qquad C_he=O(h^2).
 \tag{24}
\]

The bounded holomorphic graph construction from the direct
source applies verbatim to this value companion. It gives
\(R_h=O(h)\), with fixed derivatives \(O(h)\) on a smaller
fixed tube, and
\[
 R_h(x+h)(A_h+B_hR_h)-C_h-D_hR_h
                                  =O(e^{-c_*/h}).
 \tag{25}
\]
Its nested-domain construction uses only the invertible
Sylvester map \(R\mapsto RA_0-D_0R\), the strict stable
complement, and analytic coefficients; all hold in (23).

There is an extra order in its first columns:
\[
                              R_he=O_{\rm hol}(h^2).
 \tag{26}
\]
To prove this, put \(z=R_he\). In (25) applied to \(e\),
use (24), \(R_h=O(h)\), and \(B_h=O(h)\). The result is
\[
              z(x+h)-D_hz(x)=O(h^2)+O(h^2)\,z(x).
 \]
Cauchy's bound on a fixed smaller tube gives \(z'=O(h)\),
so \(z(x+h)-z(x)=O(h^2)\). The matrix \(I-D_h\) has a
uniformly bounded inverse. This proves (26), and Cauchy
gives its fixed derivative bounds on smaller tubes.

The slow matrix \(\widehat A_h=A_h+B_hR_h\) therefore has
block form
\[
 \widehat A_h=
 \begin{pmatrix}
 I_d+O(h^2)&I_d+O(h)\\
 O(h^2)&I_d+O(h)
 \end{pmatrix}.
 \tag{27}
\]
With the constant polynomial gauge
\[
                   H_h=\operatorname{diag}(I_d,hI_d)
 \]
we obtain the exact identity
\[
                 H_h^{-1}\widehat A_hH_h=I+hB_h^{\rm s},
                 \qquad \|B_h^{\rm s}\|\le C .
 \tag{28}
\]
All entries are holomorphic and have bounded fixed derivatives
on smaller tubes. The graph residual in (25), after this
polynomial gauge, is still exponentially small.

## 6. Recovery and the independent first-normal lift

The componentwise normalized recovery equation in (20)
has a stable principal companion: all its original roots
are \(1\), divided now by \(\tau_{\max,-n}\).
Let that companion be \(A_h^F\), and let its forcing from
the gauged companion be \(B_h^F\).

Before the gauge \(H_h\), let \(G_h^{\rm g}\) embed the
gauged slow coordinates, so
\[
       M_hG_h^{\rm g}
          =G_h^{\rm g}(x+h)\widehat A_h+O(e^{-c_*/h}).
 \]
Recovery admits a bounded holomorphic approximate embedding
\(K_h\) satisfying
\[
 K_h(x+h)\widehat A_h
       =A_h^F K_h+B_h^F G_h^{\rm g}+O(e^{-c_*/h}).
 \tag{29}
\]
For completeness this is a linear version of the same
analytic construction. Its leading Sylvester map is
\[
 {\cal L}(K)=K A_0-A_0^F K ,
 \]
which has a bounded inverse because \(A_0\) has only the
unit root and \(A_0^F\) is strictly stable. Rewrite (29) as
\[
 {\cal L}K=B_h^FG_h^{\rm g}
 +(A_h^F-A_0^F)K-K(\widehat A_h-A_0)
                  -(K(x+h)-K(x))\widehat A_h .
 \tag{30}
\]
The linear part on nested tubes loses at most
\(C(h+h/\delta)\) at erosion \(\delta\).
Choose \(K_*=\lfloor\Delta/(2Mh)\rfloor\) iterations and erosion
\(\delta=Mh\), where \(\Delta>0\) is a fixed available buffer
and \(M\) is a sufficiently large fixed constant.
Iterating (30) from zero gives a bounded geometric sum
and residual \(O(2^{-K_*})\). Reserve fixed inner tubes
for derivatives. This proves (29), including its stated
uniform bounds, without an inverse of \(J-2\).

Set
\[
 G_h=\begin{pmatrix}G_h^{\rm g}\\K_h\end{pmatrix}H_h,
 \qquad T_h=I+hB_h^{\rm s}.
 \tag{31}
\]
For the entire value companion \(M_h^{\rm v}\),
\[
 M_h^{\rm v}G_h=G_h(x+h)T_h+O(e^{-c_*/h}).
 \tag{32}
\]
The matrix \(G_h\) and its fixed derivatives are bounded.
It has a holomorphic left inverse on its image with at
most polynomial \(h^{-1}\) cost; its gauged part already
has that property.

The normalized physical normal is an independent variable.
It is not replaced by a derivative of an interpolated
slow amplitude. Explicitly, if \(f=f_hg\) at any slot, the
two jet coordinates used here are
\[
 g=f_h^{-1}f,\qquad
 hg'=f_h^{-1}\{hf'-[{\cal S}'+h\,p'/p]f\}.
 \tag{33a}
\]
This includes subtraction of the phase slope from the
retained \(h f'\) coordinate. Common-base phase normalization
alone would not give the standard jet prolongation.
Formula (33a) is an invertible triangular change of the two
independent nodal data, applied at each shifted slot.
The exact value-and-normal system is then the
derivative prolongation
\[
 \begin{pmatrix}M_h^{\rm v}&0\\h(M_h^{\rm v})'&M_h^{\rm v}\end{pmatrix}.
 \tag{33}
\]
This follows by differentiating the ordinary row equation
and then evaluating at its double physical nodes, just as
in the original source. The componentwise \(f_h\) gauge is
also differentiated; it is an exact change of both jet
coordinates.

Differentiating (32) proves that the full slow embedding is
\[
 {\cal G}_h=
 \begin{pmatrix}G_h&0\\hG_h'&G_h\end{pmatrix},\qquad
 {\cal T}_h=
 \begin{pmatrix}T_h&0\\hT_h'&T_h\end{pmatrix}
 =
 \begin{pmatrix}I+hB_h^{\rm s}&0\\
                   h^2(B_h^{\rm s})'&I+hB_h^{\rm s}\end{pmatrix}.
 \tag{34}
\]
The invariance residual and its derivatives remain exponential.
Both input vectors in (34) are free; the second is the
independent normal coordinate. Thus the dimension is
\(2(2d)=4\,6^r\), as in the original slow graph.
The embedding and its left inverse on the image have
polynomial conditioning.

## 7. Actual attraction and quantitative transport

All changes from the common-base phase packet of the
jet-adjoint source to the componentwise gauge used here
are bounded, with bounded inverse, on the fixed tubes.
For a slot with fixed offset \(\ell\) their exponential
factor is
\[
       \exp\{[{\cal S}(x+\ell h)-{\cal S}(x)]/h\},
 \]
which has a bounded analytic extension to \(h=0\).
The scalar \(p\) is a unit. In the normal blocks the
corresponding derivative is multiplied by \(h\), so it
does not introduce an exponential or uncontrolled factor.

Before the polynomial gauge \(H_h\), the constructed slow
graph has bounded frames and a strictly stable complement.
For recovery this complement is triangular over the gauged
stable complement, with stable diagonal \(A_0^F\).
The differentiated complement is again stable, with the
off-diagonal derivative blocks multiplied by \(h\).
The fixed-block stability proof from the slow-graph source
therefore applies to the whole system. Its transverse
propagator is bounded by \(Ce^{-c(j-l)}\). The graph
residual forces it by at most \(e^{-c_*/h}{\cal B}_N^*\),
up to fixed polynomial factors.

Consequently, after a fixed positive left buffer, the actual
whole packet is exponentially close to the graph (34).
Its slow coordinate has at most polynomial times
\({\cal B}_N^*\) norm. This retains the original left
packet: the homogeneous transverse term is
\(Ce^{-c(j-j_*)}\) times that packet, not an asserted zero.

From (34), both \({\cal T}_h\) and its inverse have norm
at most \(1+Ch\). A product over \(O(h^{-1})\) rows, in
either direction, is therefore bounded by a constant.
The polynomial conditioning at its two ends yields the
claimed polynomial slow-packet cost.
Summing the exponentially small forced errors over the
same number of rows preserves an exponential bound after
decreasing its constant. Applying this to the actual
slow coordinates and then returning to the original
packet proves (6).

A previously established lower slow norm can therefore
be propagated with polynomial loss, provided it exceeds
the displayed exponential error. This note does not
establish such an initial norm, its leading coefficient,
or a nonzero value under the original scalar closing.
It also does not prove that the normalized normal equals
the derivative of a scalar amplitude. The independent
normal copy in (34) is exactly why that conclusion has
not been made.

## 8. Coverage and direct sources

The earlier slow-graph theorem retains an arbitrary
\(O(h)\) perturbation of a square-zero Jordan block and
therefore gives a subexponential transport cost.
The new input here is the exact even midpoint identity
of the original operators and its second-order
constant-amplitude consequence for the full source module.
The analytic graph and stable-attraction constructions
are reused with this additional structure.

Complete direct-source reads are fresh or retained at
the following unchanged pins; used implications and
hashes were checked:

* [Original finite-band operator identities](research_unit_turn_finite_band_branching_operator.md),
  SHA256 31d9f574c7dc3aaac07e4eb50c131b3328be46b3c2a2ef46f9dae7f0c4ddb9cb:
  both ordered recurrences and their exact full-algebra scope.
* [Ordinary terminal row lift](research_terminal_twist_bulk_transfer_bound.md),
  SHA256 fca96865315f21dc9961be89061cc6c3a292b2b563e7ded756e86c3438ef5bde:
  literal finite-shift coefficients, ordinary residuals and
  physical first-normal equations.
* [Literal filled-leaf product source](research_filled_leaf_endpoint_product_upper_bound.md),
  SHA256 5a5f9be510823289b97c1c4df6104d95156b43a881fe148adf592ed5b5adc844:
  the ordered \(d(J)(D_{-n}-c_0)-s^2E(J)\) module, full
  gauged channels, recovery and original initialization scope.
* [Normalized whole jet and signed phase](research_filled_leaf_normalized_jet_adjoint.md),
  SHA256 49e6f5494df6de3b1fa0f6ad05d17ef0712fc89377cb3695ac737094bf5f9a70:
  actual simultaneous prefix budget, phase constant, signed
  dominant root and exact normal-coordinate convention.
* [Holomorphic slow graph and attraction](research_filled_leaf_slow_graph_reduction.md),
  SHA256 f6551febb73c55f90752e797f7c593bb169d8cd65c6756e5d001f5fc3cc7507d:
  fixed holomorphic splitting, finite analytic graph iteration,
  stable block estimates and retained independent normals.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test or build
was run. Adopted notes and public manuscripts are unchanged.
