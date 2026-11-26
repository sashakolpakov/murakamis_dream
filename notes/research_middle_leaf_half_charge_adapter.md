# The single middle Newton factor is an original half-charge observation

Private written proof, 17 November 2026.

The odd single-middle observation is the top interpolation coefficient
already retained in [F]. At even levels it is exactly the central
normal defect of that same original interpolation problem. This pays
the normal needed to use [F]'s whole-outside-period bounds at both
parities. An original middle path then has at most two interfaces;
its internal contractions are explicit polynomial factors. Every
remaining exterior contraction is retained, not estimated here.

## 1. Original normalization and the exact adapter

Use the conventions of [C,F]:
\[
 D=N-1,\quad m=\lfloor N/2\rfloor,\quad L=D-m,\quad
 q=e^{\pi i/N},\quad \eta=(-1)^D,\quad N\ge2,
\]
\[
 s_j=2\sin(j\pi/N),\quad S_j=\prod_{a=1}^js_a,\quad
 c_a=2\cos((2a+1)\pi/N),\quad
 e_j(z)=S_j^{-2}\prod_{a<j}(c_a-z),
\]
\[
 P_N=2T_N(z/2)+2,\quad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f,\quad
 K_N(z,\zeta)=\sum_{j=0}^D e_j(z)e_j(\zeta),\quad A=e_L.
 \tag{1}
\]
Only traced variables are reduced. Outside colors remain ordinary
polynomial variables. The original crossing has values
\[
 R(c_a)=q^{D^2/2}(-1)^a q^{a(a+1)},\qquad
 \chi_N=q^{D^2/4}.
 \tag{2}
\]
All powers below are the full physical powers, including negative
ones. For each integer \(n\), define the actual leaf coupon
\[
 \mathcal L_{n,N}(\zeta)
       =\phi_N^{(z)}[R(z)^n A(z)K_N(z,\zeta)].
 \tag{3}
\]

Put \(\Omega=\mathbb C\setminus[2,\infty)\) and use the original
squared-inverse-cosine branch, holomorphic through \(z=-2\), to set
\[
 h_{n,N}(z;\zeta)
   =e^{inN\arccos(-z/2)^2/(4\pi)}K_N(z,\zeta).
 \tag{4}
\]
Let \(I_{n,N}(z;\zeta)\) be its ordinary interpolant at all distinct
physical nodes: degree at most \(m\) when \(N=2m+1\), and less than
\(m\) when \(N=2m\). Define
\[
 Q_{\rm d}(z)=2T_m(z/2)\quad(N=2m),\qquad
 \mathscr D_{n,N}(z;\zeta)
       =\frac{h_{n,N}(z;\zeta)-I_{n,N}(z;\zeta)}{Q_{\rm d}(z)}.
 \tag{5}
\]
The quotient is holomorphic at every distinct node. It is precisely
the even normal defect in [F, (18)]. At odd levels write
\(\ell_{n,N}(\zeta)=[z^m]I_{n,N}(z;\zeta)\).

**Exact adapter.** For every integer \(n\), every outside color,
and all \(N\ge2\),
\[
 \boxed{\quad
 \mathcal L_{n,N}(\zeta)=
 \begin{cases}
  (-1)^mN\chi_N^n\ell_{n,N}(\zeta),&N=2m+1,\\
  2N(-1)^m\chi_N^n\mathscr D_{n,N}(c_*;\zeta),&N=2m,
 \end{cases}\qquad c_*=-2\cos(\pi/N).
 \quad}
 \tag{6}
\]
Every ordinary outside derivative satisfies the same identity.

*Proof.* With \(t_a=\pi-(2a+1)\pi/N\), direct expansion gives
\[
 R(c_a)^n=\chi_N^n e^{inNt_a^2/(4\pi)}.
 \tag{7}
\]
The odd simple node has \(t=0\), so its carrier is also included.
By the original Frobenius rule
\(\phi_N(e_i e_j)=\mathbf1_{i+j=D}\), multiplication by \(A\)
extracts the Newton coefficient at index \(D-L=m\).

At odd levels its first \(m+1\) Newton nodes are distinct. This
coefficient depends only on their values. The leading coefficient
of \(e_m\) is \((-1)^m/N\), since \(S_m^2=N\).
Equations (7) and ordinary divided differences give the first line.
This is the top-degree term in [F, (24)], with its carrier restored.

At even levels the first \(m\) nodes are distinct and the next
node is the repeated central node \(c_m=c_{m-1}=c_*\). Moreover
\[
                  e_m(z)=\frac{(-1)^m}{2N}Q_{\rm d}(z),
 \tag{8}
\]
because \(S_m^2=2N\). Subtracting \(I_{n,N}\) leaves
\(Q_{\rm d}\mathscr D_{n,N}\). The next confluent Newton
coefficient is consequently \(2N(-1)^m\mathscr D_{n,N}(c_*;\zeta)\).
It uses the central derivative, not just values. The derivative of
the Gaussian in (4) there is
\[
 \frac{d}{dz}\log e^{inN\arccos(-z/2)^2/(4\pi)}\bigg|_{c_*}
                       =\frac{in}{2s_1},
 \tag{9}
\]
which is exactly the original crossing normal [C, (16)]. This
also verifies negative powers. Thus the confluent coefficient is
the physical coefficient required by the trace. This proves (6).
All formulas are coefficientwise in ordinary outside variables, so
differentiation there commutes with them. \(\square\)

## 2. Whole-period bounds for the actual coupon

For a fixed integer \(n\ge3\), let \(t_n\) and \(M_n\) be the
original complete half-charge saddle and its real action from [F]:
\[
 nt_n+2i\operatorname{asinh}\tan(t_n/2)=\pi,\qquad
 M_n=\Re\{\psi(t_n,0)+int_n^2/(4\pi)-it_n/2\}.
 \tag{10}
\]
There are \(c,B,h_*>0\) such that, for every fixed ordinary
derivative order \(k\), there are \(C_k,a_k\) with
\[
 \boxed{\quad
 |\partial_\zeta^k\mathcal L_{n,N}(-2\cos(u+iv))|
 \le C_kN^{a_k}
       e^{N\{M_n-c(1-\cos u)+Bv^2\}},
 \quad |u|\le\pi,\quad |v|\le h_*.
 \quad}
 \tag{11}
\]
The estimate is uniform in the outside angle and in the level
parity, for all sufficiently large levels. It includes the
ordinary derivative at both spectral endpoints.

Indeed [F, Theorem 4] bounds the exact normal defect uniformly
over every physical node, including \(c_*\), with all ordinary
outside derivatives. The second line of (6) changes only its
polynomial prefactor. The same theorem explicitly bounds the odd
top trace [F, (24)], giving the first line. Its proof retains the
whole original observation contour, physical omitted rows, normal
terms and vertical connectors; no local packet is extrapolated to
the whole period here.

For negative integers with \(|n|\ge3\), (11) holds with
\(M_{|n|}\). The polynomials \(A,K_N,P_N\) and the trace are real.
The physical values (7), and the central normal (9) when needed,
are conjugated by \(n\mapsto-n\). These are all the data consumed
by the single-\(A\) observation in (6). Hence exactly
\[
 \mathcal L_{-n,N}(\zeta)
                 =\overline{\mathcal L_{n,N}(\overline\zeta)}.
 \tag{12}
\]
Conjugation sends \(v\) to \(-v\) in (11), leaving its upper
exponent unchanged. The algebraic identity (6) holds also for
\(n=0,\pm1,\pm2\); no estimate (11) is claimed for those powers.

## 3. Exact path interiors and all remaining interfaces

Select a path of original edges and replace each selected kernel
by its literal middle summand \(A(z_v)A(z_w)\). This is a finite
Newton term, not just one of the two middle exponentials. Suppose
every internal path vertex is traced and has degree two in the
original graph. The arbitrary exterior depends on the remaining
variables; any extra direct dependence on a traced path vertex
must instead remain in [C]'s joint spectator. An internal vertex
has no remaining incident kernel, so its contraction is
\[
 \boxed{\quad
 \phi_N(R^nA^2)=
 \begin{cases}
 R(-2)^n,&N\text{ odd},\\
 -2inR(c_*)^n/s_1,&N\text{ even}.
 \end{cases}
 \quad}
 \tag{13}
\]
These identities hold for every integer \(n\). In particular an
even-level zero-power internal vertex kills that entire path term.

The odd identity is [C, (7)]. For the even identity put
\(\tau=\sum_{a<m-1}(c_*-c_a)^{-1}\), as in [C]. Since
\(Q_{\rm d}\) has its simple roots at these \(m\) distinct nodes,
\[
 2\tau=Q_{\rm d}''(c_*)/Q_{\rm d}'(c_*)=c_*/s_1^2.
 \tag{14}
\]
The last equality is the Chebyshev differential equation at a root.
Insert (14) into [C, (12)] with \(r=2,f=1\), using
\(\eta=-1\) and \(E=2/s_1\), to obtain (13).
This includes \(N=2\), where the sums in \(\tau\) are empty.
For a fixed path and fixed powers, its internal scalar has at most
polynomial size: each even factor is at most \(|n|N/2\), while
each odd factor has modulus one.

At a traced path endpoint with one surviving original edge, taking
that endpoint's trace transmits exactly \(\mathcal L_{n,N}(\zeta)\)
to the opposite outside variable of that edge. Thus the path has
at most two such interfaces. The entire exterior may be a joint
polynomial or an original coupled contraction in those variables:
the transmitted coupons are multiplied into it before its remaining
traces are taken. No factorization of that exterior is used.

An endpoint with no surviving edge gives the exact scalar
\(\phi_N(R^nA)\), of polynomial size for fixed \(n\), by
[C, (8),(13),(23)]. An ordinary untraced endpoint instead keeps
its literal factor \(A(\zeta)\); no physical reduction is imposed
there. At a prescribed complete outside endpoint this factor is
\[
 A(-2)=1\quad(N\text{ odd}),\qquad
 A(-2)=\{N\sin^2(\pi/(2N))\}^{-1}\quad(N\text{ even}),
 \tag{15}
\]
again polynomial in size. The even formula follows from (8),
\(e_m(-2)=1/N\), and [C, (14)].

These reductions may be performed for several paths in one graph.
All common exterior variables and product-rule normals remain in
their original traces. If the degrees of a traced middle vertex or
its extra attachments exceed this path scope, use [C]'s actual
value/normal operator on the joint spectator; do not replace that
operator by the scalar (13).

For example, if a surviving edge joins two traced single-middle
endpoints directly, retain its exact joint observation
\[
 \mathcal J_{n,p,N}
   =\phi_w[R(w)^pA(w)\mathcal L_{n,N}(w)].
 \tag{16}
\]
For \(|n|,|p|\ge3\), (11) and [C]'s original single-\(A\)
rows give
\[
       |\mathcal J_{n,p,N}|
        \le C N^a e^{N\min(M_{|n|},M_{|p|})}.
 \tag{17}
\]
At odd levels the row has total value weight at most \(N\).
At even levels its value weights have polynomial total size and
its one central derivative has polynomial coefficient; (11)
bounds that derivative as well. This first gives the exponent
\(M_{|n|}\). Symmetry of the original kernel gives the other
bound and hence (17). No independent-observation assumption is made.

For separate interfaces, (11) gives a product bound on a product
of fixed outside strips, with exponent the sum of their displayed
upper exponents. This bounds the transmitted co-source itself.
It does not bound its subsequent contraction with an arbitrary
exterior array or its final signed scalar.

## 4. Scope and complete direct sources

The cutoff theorem already gives the local multiple-middle
identities and their full-normal meaning. The free-boundary theorem
already supplies a whole-period half-charge estimate. The new adapter
(6) identifies the even single-middle coupon with its bounded normal
defect, alongside the retained odd top coefficient, and (13)--(17)
give their literal path-interface consequence.

The path term is not asserted to represent every analytic midpoint
current: the original cutoff forcing is \(A\otimes e_{L+1}\), a
different insertion. Nor does a failed angle-capacity test imply
vanishing. No branching multi-leg estimate, geometric action gap for
the remaining exterior, nonzero relative-cycle coefficient, or new
filling theorem follows here.

Both complete direct texts were read in full and their used
implications checked at these versions:

* [C: Exact cutoff and full middle-factor observations](research_cutoff_cluster_exact_reduction.md),
  SHA256 50d126430f711407c5815d840c401c30fef0c09f018fad1a5dfbef60eca81374.
* [F: Original half-charge observation with free outside color](research_free_boundary_half_charge_observation.md),
  SHA256 871e2a286f6c8eb90572badf45d454e9c0042537719ce8b3881d22dc5d7fff5b.

Only written mathematics, source reads and hashes were used.
No mathematical program, numerical experiment, test or build was run.
Frozen notes and public papers were unchanged.
