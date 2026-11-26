# The actual prefix order and its first normal layer

Private written proof, 19 November 2026. Author-final for independent review.

The original cut pairing bounds the pole of the inverse prefix
coordinate by one. Consequently the entire root intertwiner, not
only its closing trace, is determined by the value and first
meridian derivative of its actual reduced matrix. The part lost by
the root reduction is a square-zero ideal. The admissible root
reduced matrices form a self-annihilating subalgebra for the polar
part of the original source pairing.

These are statements about the actual finite source and its
common-meridian germ. They do not give a positive pairing, an
elliptic kernel, or a nonzero prescribed closing. The complete
directs are L, the physical endpoint duality, and R, the actual
prefix algebra and pointed source. All order and first-normal
arguments are proved below.

## 1. The two coordinates and the original source

Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,
 \quad m=r+1\ge2,\quad M=e^\mu,\quad x=-M/q.
 \tag{1}
\]
The quantum root is fixed. Let \(U\) be the remaining \(r\)-head
occupation space, with its actual ordered totals \(E,F,K\). Put
\[
 K(M)=M^rK_0,\qquad K_0^N=\varepsilon I,
 \quad\varepsilon=(-1)^{(N+1)r},\qquad
 \mathcal A=\{H\in\operatorname{End}(U):[K_0,H]=0\}.
 \tag{2}
\]
This is a fixed direct sum of full matrix algebras. No occupation
index or remaining matrix block is replaced by a scalar.

L identifies every \(H\in\mathcal A\) with the unique actual total
intertwiner \(W_H(M)\) having physical highest block \(H\). The
identification and its inverse are holomorphic wherever the first
head coefficients
\[
                 e_a=MQ^{-a}-M^{-1},\qquad 1\le a\le d,
 \tag{3}
\]
are nonzero. This includes \(M=1\). Write \(\star_\mu\) for the
transported product, so \(W_{H\star_\mu J}=W_HW_J\).
L's opposite physical endpoint is the holomorphic linear unit
\[
             \mathscr L_\mu H=(W_H)_{dd}.
 \tag{4}
\]
With \(g_\mu=K(M)^{1-N}\), its exact source identity is
\[
 \operatorname{Tr}(g_\mu(H\star_\mu J))
       =\operatorname{Tr}(g_\mu H\mathscr L_\mu J).
 \tag{5}
\]
Both \(\mathscr L_\mu\) and its inverse are regular at zero.

Keep R's literal finite prefix and quotient:
\[
 S(M)=\sum_{a=0}^d\frac{(x^{-1}L_1F)^a}{f_a},\qquad
 f_a=\prod_{j=1}^a(1-Q^j),\qquad
 \mathscr B_\mu H=p_0S(M)^{-1}W_H(M)i_0.
 \tag{6}
\]
Thus \(\mathscr B_\mu\) is a holomorphic linear map on
\(\mathcal A\), with every original prefix coefficient and cap.
It satisfies
\[
 \mathscr B_\mu(H\star_\mu J)
       =(\mathscr B_\mu H)(\mathscr B_\mu J),
                 \qquad\mathscr B_\mu I=I.
 \tag{7}
\]
It is not presumed invertible at \(\mu=0\).

For clarity its finite construction can also be read directly from
L. If \(C_a(H)=(W_H)_{a0}\), then
\[
 C_0=H,\quad C_{a+1}=-e_{a+1}^{-1}K^{-1}[E,C_a],\qquad
 \mathscr B_\mu H=
 \sum_{a=0}^d\frac{(-1)^aQ^{a(a-1)/2}x^{-a}}{f_a}F^aC_a(H).
 \tag{8}
\]
Only the nonzero first-head arrows and \(f_1,\ldots,f_d\) are
divided by in this formula.

Set
\[
 D_\mu=\frac{D_N(M)}{D_N(MK(M))},\qquad
 D_N(z)=\frac{z^N-z^{-N}}{z-z^{-1}}.
 \tag{9}
\]
The Laurent-polynomial convention for \(D_N\) is retained.
R proves the exact original highest-cut and pivotal source
\[
 \operatorname{Tr}(g_\mu H)
       =\operatorname{Tr}(D_\mu\mathscr B_\mu H).
 \tag{10}
\]
The right side is first interpreted generically and then by its
prescribed continuation. Since \(D_\mu\) is a function of \(K_0\),
it is central in \(\mathcal A\).

## 2. A simple pole for the entire inverse coordinate

Use the ordinary bilinear trace pairing on \(\mathcal A\). For a
linear map \(T\), define its transpose by
\[
                 \operatorname{Tr}(A\,T H)
                    =\operatorname{Tr}((T^*A)H).
 \tag{11}
\]
There is no complex conjugation. This trace pairing is perfect on
each Cartan matrix block, so \(T^*\) is uniquely defined. Put
\(\mathcal G_\mu X=Xg_\mu\) and \(\mathsf D_\mu X=D_\mu X\).
Equations (5), (7), and (10), applied to the actual product, give
\[
 \boxed{\qquad
 \mathcal G_\mu\mathscr L_\mu
       =\mathscr B_\mu^*\mathsf D_\mu\mathscr B_\mu.
 \qquad}\tag{12}
\]
Indeed the source of \(W_HW_J\) is both
\(\operatorname{Tr}(g_\mu H\mathscr L_\mu J)\) and
\(\operatorname{Tr}(D_\mu(\mathscr B_\mu H)(\mathscr B_\mu J))\).
Move the latter's central \(D_\mu\) and take the transpose in
(11). Equality for every \(H\) proves (12), including its order.

On a punctured sufficiently small meridian disk the scalar on each
Cartan block in (9) is a unit. The left side of (12) is invertible.
Thus \(\mathscr B_\mu\) is injective, and hence bijective in the
same finite dimension. In particular generic surjectivity does
not require a separate recursive Cartan inversion. Equation (12)
then gives the explicit inverse
\[
 \boxed{\qquad
 \mathscr B_\mu^{-1}
   =\mathscr L_\mu^{-1}\mathcal G_\mu^{-1}
                          \mathscr B_\mu^*\mathsf D_\mu.
 \qquad}\tag{13}
\]

The source matrix has the exact expansion
\[
 \begin{split}
 D_\mu&=\frac{d_{-1}}\mu+d_0+O(\mu),\\
 d_{-1}&=\frac{K_0-K_0^{-1}}{2\varepsilon m},\qquad
 d_0=\frac{K_0+K_0^{-1}}{2\varepsilon}.
 \end{split}\tag{14}
\]
To check it, replace its denominator by
\(\varepsilon(e^{mN\mu}-e^{-mN\mu})\) and its numerator by
\(D_N(e^\mu)(e^{m\mu}K_0-e^{-m\mu}K_0^{-1})\), using (2).
All other factors in (13) are holomorphic at zero. Consequently
\[
 \boxed{\quad\mathscr C_\mu:=\mu\mathscr B_\mu^{-1}
                      \text{ is holomorphic at }\mu=0.\quad}
 \tag{15}
\]
This is an operator statement for the full inverse coordinate,
not just a cancellation after one closing trace.

## 3. Exact admissibility and whole-intertwiner first jets

Let \(\mathcal O\) be the ring of holomorphic germs in the fixed
parameter \(\mu=\Log M\), and set
\[
 \mathcal A_{\mathcal O}=\mathcal A\otimes\mathcal O,
 \qquad\mathcal I=\mathscr B(\mathcal A_{\mathcal O}),
 \qquad V=\operatorname{im}\mathscr B_0\subset\mathcal A.
 \tag{16}
\]
It follows from (15) that
\[
       \mu\mathcal A_{\mathcal O}\subset\mathcal I
                              \subset\mathcal A_{\mathcal O}.
 \tag{17}
\]
For the left inclusion, \(\mu Z=\mathscr B(\mathscr C Z)\).
Write
\[
 \mathscr B_\mu^{-1}=\frac{\mathscr R}{\mu}+\mathscr Q+O(\mu),
 \qquad\mathscr B_\mu=\mathscr B_0+\mu\mathscr B_1+O(\mu^2).
 \tag{18}
\]
Multiplying in both orders gives
\[
 \mathscr R\mathscr B_0=\mathscr B_0\mathscr R=0,
 \quad\mathscr B_0\mathscr Q+\mathscr B_1\mathscr R=I,
 \quad\mathscr Q\mathscr B_0+\mathscr R\mathscr B_1=I.
 \tag{19}
\]
In particular
\[
                      \ker\mathscr R=V.
 \tag{20}
\]
One inclusion follows from the first identity; if
\(\mathscr R Z=0\), the second gives \(Z=\mathscr B_0\mathscr Q Z\).

Hence the exact image order is
\[
 \boxed{\qquad
 \mathcal I=\{Z\in\mathcal A_{\mathcal O}:Z(0)\in V\}
           =V\otimes\mathcal O+\mu\mathcal A_{\mathcal O}.
 \qquad}\tag{21}
\]
Equivalently, an analytic proposed reduced matrix is the prefix
of an analytic actual intertwiner if and only if
\(\mathscr RZ(0)=0\). Indeed (18) has only that possible pole.
There are no successive higher-order divisibility conditions.
The condition remains a full matrix condition on the extensive
remaining-head seed.

There is a corresponding physical co-source for an arbitrary
analytic Cartan-preserving reduced mark \(Z(\mu)\):
\[
 \Xi_Z=\mathscr L_\mu\mathscr B_\mu^{-1}Z
        =\bigl(\mathscr B_\mu^*(D_\mu Z)\bigr)g_\mu^{-1},
 \qquad
 \operatorname{Tr}(D_\mu(\mathscr B_\mu H)Z)
                      =\operatorname{Tr}(g_\mu H\Xi_Z).
 \tag{21a}
\]
Its residue is exactly \(\mathscr L_0\mathscr RZ(0)\).
It is holomorphic if and only if \(Z(0)\in V\). Thus (21a)
transports an actual reduced marked closing to the opposite
physical endpoint, but does not declare an arbitrary local window
admissible. If \(Z=Z_0+\mu Z_1+\cdots\), its unrestricted finite
part is
\[
 \mathscr L_0(\mathscr RZ_1+\mathscr QZ_0)
                         +\mathscr L_1\mathscr RZ_0,
              \qquad\mathscr L_1=\partial_\mu\mathscr L|_0.
 \tag{21b}
\]
Both moving-mark and moving-endpoint normal terms remain.

For such an actual reduced family write
\(Z(\mu)=Z_0+\mu Z_1+O(\mu^2)\). Its entire physical root seed is
\[
 \boxed{\qquad H(0)=\mathscr RZ_1+\mathscr QZ_0.\qquad}\tag{22}
\]
Applying L's finite highest-block reconstruction then recovers
every block of \(W_H(0)\). Thus the first meridian jet of the
actual reduced matrix determines the whole root intertwiner.
This does not mean its first normal needs no further data:
\(H'(0)\) generally uses \(Z''(0)\) as well. Higher fixed jets
follow by the ordinary product rule in \(H=\mathscr C Z/\mu\).
No quantum parameter or forced outward arrow is differentiated.

## 4. The lost root ideal is square-zero

The map \(\mathscr B\) is an algebra isomorphism from the physical
intertwiner order, expressed with \(\star_\mu\), to \(\mathcal I\).
After specializing it identifies the whole root intertwiner algebra
with \(\mathcal I/\mu\mathcal I\). Reduction to the ordinary root
matrix has kernel
\[
 \mathcal K=\mu\mathcal A_{\mathcal O}/\mu\mathcal I,
 \qquad
 0\longrightarrow\mathcal K\longrightarrow
 \mathcal I/\mu\mathcal I\longrightarrow V\longrightarrow0.
 \tag{23}
\]
Every factor in the numerator of \(\mathcal K^2\) has one
\(\mu\); (17) gives
\(\mu^2\mathcal A_{\mathcal O}\subset\mu\mathcal I\). Therefore
\[
                         \boxed{\quad\mathcal K^2=0.\quad}\tag{24}
\]
In physical coordinates this is the kernel of \(\mathscr B_0\)
with the actual product \(\star_0\), not ordinary multiplication
of the highest blocks. Its unit kernel is consequently additive:
\((1+k)(1+l)=1+k+l\), \((1+k)^{-1}=1-k\) for \(k,l\in\mathcal K\).

There is also an explicit splitting in the fixed prefix coordinates.
By (21), constant matrices in \(V\) belong to \(\mathcal I\).
The data of a class modulo \(\mu\mathcal I\) are exactly
\[
                        (Z_0,[Z_1])\in V\oplus(\mathcal A/V).
 \tag{25}
\]
The multiplication is
\[
 (b,[c])(b',[c'])=(bb',[bc'+cb']).
 \tag{26}
\]
It is well-defined because \(V\) is a subalgebra, by (7).
This is a split square-zero extension with its literal bimodule;
it does not erase that bimodule or its possible source value.

## 5. The polar pairing and reciprocal blocks

Define the symmetric bilinear, possibly degenerate form
\[
                  \beta(A,B)=\operatorname{Tr}(d_{-1}AB).
 \tag{27}
\]
Its central coefficient is exactly the residue of the original
source. Taking the residue of (13) gives
\[
 \mathscr R=\mathscr L_0^{-1}\mathcal G_0^{-1}
                              \mathscr B_0^*\mathsf d_{-1},
 \qquad\mathsf d_{-1}X=d_{-1}X.
 \tag{28}
\]
The first two factors are units. Thus \(\ker\mathscr R\) is the
annihilator of \(\operatorname{im}\mathscr B_0\) for (27).
Combining this with (20) proves the source-specific identity
\[
                         \boxed{\quad V=V^{\perp_\beta}.\quad}\tag{29}
\]
In particular \(V\) contains the radical of \(\beta\).

Here is the exact pair decomposition, without a new spectral
projector premise. The actual total Casimir
\(\Omega_\Sigma=F_\Sigma E_\Sigma+qK_\Sigma+q^{-1}K_\Sigma^{-1}\)
commutes with all total generators. R's relations
\(S^{-1}F_\Sigma S=F_1\), \([S,K_\Sigma]=0\), \(Si_0=i_0\),
and \(p_0F_1=0\) give
\[
         \mathcal B_m(\Omega_\Sigma)
                     =-MK-M^{-1}K^{-1}.
 \tag{30}
\]
At the root two actual weights \(\chi,\psi\) have the same
number \(-\chi-\chi^{-1}\) exactly when \(\psi=\chi\) or
\(\psi=\chi^{-1}\). Polynomial interpolation on these distinct
numbers puts every inversion-pair projector \(P_{\mathfrak o}\)
in \(V\), using the actual polynomial intertwiner
\(p_{\mathfrak o}(\Omega_\Sigma)\). It is unnecessary to assert
that this full polynomial coupon is itself a projector.
The matrices \(P_{\mathfrak o}\) are central in \(\mathcal A\),
so \(V\) decomposes over these pairs.

Each physical Cartan weight space has dimension
\(n=N^{r-1}\): choose \(r-1\) occupations freely and the last
is uniquely fixed modulo \(N\). On a nonself pair,
\[
 \mathcal A_{\mathfrak o}
    =\operatorname{End}(U_\chi)\oplus\operatorname{End}(U_{\chi^{-1}}),
 \quad
 \beta((A,B),(C,D))
       =\frac{\chi-\chi^{-1}}{2\varepsilon m}
                          \operatorname{Tr}(AC-BD).
 \tag{31}
\]
This form is nondegenerate. Equation (29) therefore gives
\(\dim V_{\mathfrak o}=n^2\), half the displayed space.
It also identifies \(\mathcal A_{\mathfrak o}/V_{\mathfrak o}\)
with \(V_{\mathfrak o}^*\) by (27). For a self weight \(\chi=\pm1\),
the entire block is in the radical and hence in \(V\): no root
matrix is lost there. These are bilinear statements, not
Hermitian orthogonality or a positive resolution. A half-dimensional
subalgebra need not be the graph of an isomorphism between the
two matrix blocks.

The source in the root coordinates (25) is exactly
\[
 \boxed{\qquad
 \tau_0(b,[c])=\operatorname{Tr}(d_0b)+\operatorname{Tr}(d_{-1}c).
 \qquad}\tag{32}
\]
The residue vanishes because \(I\in V\) and (29) gives
\(\beta(b,I)=0\). Changing \(c\) by an element of \(V\) leaves
(32) unchanged for the same reason. Thus the normal layer is
retained as a genuine part of the original cut, even when the
ordinary reduced root matrix misses it. Formula (32) has exactly
the original factors \(2\varepsilon\) and \(m\), not a freely
chosen normalization of the paired sheets.

## 6. Finite conditioning, true normals, and scope

The construction is entirely finite and keeps every head cap.
It also gives an exponential, rather than superexponential, bound
for the regularized inverse. Fix the width and
\(0<\eta<\pi/m\), and set \(\mu=u/N\), \(|u|\le\eta\).
L bounds highest reconstruction, \(\mathscr L^{\pm1}\), and the
finite prefix coefficients by \(e^{CN}\). In particular (6),(8)
give \(\|\mathscr B\|\le e^{CN}\). One may use the
Hilbert--Schmidt norm on each Cartan matrix block to take the
transpose in (11); passage to occupation operator norm costs only
a polynomial in \(N\) at fixed width. Also \(g^{\pm1}\) are bounded
on this collar.

The explicit expression used in (14) gives
\(\|\mu D_\mu\|\le C\) there, with its removable value at zero:
\(D_N(e^{u/N})=O(N)\) and \(\sinh(m u)/u\) is bounded away from
zero on the smaller disk. Equation (13) consequently proves
\[
                   \|\mathscr C_\mu\|\le e^{CN}.
 \tag{33}
\]
On nested collars, every fixed \(j\)-th \(\mu\) derivative of
\(\mathscr C\) costs at most \(C_jN^je^{CN}\), by Cauchy's formula.
These bounds include the actual meridian dependence of the prefix,
totals, pivot, and endpoint maps. They are not zero-exponential-rate
estimates for a geometric kernel.

All crossing and zero-framing scalars included in an actual word
remain in its physical seed and reduced matrix. A separately
prescribed scalar remains outside (10), with its own product-rule
derivatives. Nothing here differentiates the quantum root or resets
a missing endpoint arrow.

The result gives a single residue condition for analytic source
admissibility, a first-jet reconstruction of the whole root operator,
and the exact square-zero normal layer of its reduction. It does
not estimate the extensive remaining seed of a particular braid.
The reciprocal blocks in (31) are whole physical Cartan blocks,
not selected geometric eigenflags. No local phase, geometric
window transport, positive pairing, or nonzero prescribed closing
is inferred from (29) or from perfect cut duality.

## Complete direct-source pins

* L: notes/research_lowest_physical_block_cut_pairing.md,
  327 lines, SHA256
  be1d3960c0144b69308879d710076b5037e3253ac2ea4b0f788f28616c47d90f.
* R: notes/research_actual_reduced_braid_source.md,
  330 lines, SHA256
  9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.

Both complete directs were freshly whole-read nontruncated in the
active author sequence. The entire matching final was freshly
read back nontruncated, every used implication checked, and all
three pins renewed before freezing. Independent review and parent
adoption remain separate. Only written mathematics and text/hash
operations were used. Frozen and public files were unchanged.
