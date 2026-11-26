# Actual fixed-width Gauss boundary kernels, their branches and vacuum layer

Private written proof, 18 November 2026.

The initialized first column of the universal Gauss operator admits an
exact width recursion and an exact finite divided-difference lift.
For every fixed number of tail heads these determine its vacuum
normalization, its microscopic limit, and actual exponential branches
on explicitly separated sectors. No spectral channel sum is introduced.
The original vacuum forcing remains in the recursion.

A fixed zero-free disk at the origin does not persist to three tail
heads: the actual normalized column has zeros at distance \(O(N^{-1})\).
Thus the wider initializer must retain its branches and their
confluent derivatives. This is a boundary-kernel theorem, not a
higher-dimensional Goursat theorem or a closed-source estimate.

## 1. Actual spaces and all-width first columns

Use the fixed root and complete meridian:
\[
 c_0=2\pi i,\quad Q=e^{c_0/N},\quad q=e^{c_0/(2N)},\quad
 d=N-1,\quad x=-q^{-1},\quad f_a=(Q;Q)_a.
\]
Fix an integer number \(r\geq2\) of tail heads. The universal actual
operator \(A_N^{(r)}=q_FE_\Sigma^d i_d\) and its place in the original
opposite kernel are those of [G]. At completeness its ordered formula is
\[
 A_N^{(r)}=(-1)^dN\sum_{n=0}^d
            \frac{(-1)^nq^{n^2}}{f_n^2}F^nE^nK^{d-n}.          \tag{1}
\]
Here \(E,F,K\) are the actual ordered totals on these \(r\) heads.

Work in integer degree \(0\leq T\leq d\), and initialize on
\[
       v_{\rm in}=|0,\ldots,0,T\rangle,\qquad
       \sigma_N=(T+1)/N\in I\Subset(1/2,1).
\]
Put
\[
 C=Q^{-T-1},\quad K_{r,T}=x^rQ^{-T},\quad
 s=r-1,\quad p=r-2,\quad \alpha=x^s.
                                                                  \tag{2}
\]
The letter \(C\) is the two-tail reference clock and is not the
total Cartan \(K_{r,T}\) when \(r\ne2\).

For the first \(s\) heads, the literal divided vacuum descendants are
\[
 \mathbf v_a=\frac{F_{[1,s]}^a}{f_a}|0,\ldots,0\rangle
   =\sum_{\substack{b_1+\cdots+b_s=a\\b_i\geq0}}
               x^{-\sum_{i=1}^s(i-1)b_i}|b_1,\ldots,b_s\rangle.
                                                                  \tag{3}
\]
We only use \(a\leq T<N\), so every factorial and head index is
physical. To prove (3), order the \(Q\)-multinomial expansion of
\(\sum_iK_1^{-1}\cdots K_{i-1}^{-1}F_i\) with the smaller-index
factor to the left. Its rightmost factors act while their preceding
heads still have occupation zero. The multinomial \(f_a/\prod f_{b_i}\)
cancels the individual raising products and leaves exactly (3).

The prefix vacuum is killed by its total \(E\) and has Cartan
\(\alpha\). In particular \(E\) on \(v_{\rm in}\) lowers only the last
head. Expanding the total \(F\) between this prefix and the last head,
as in [B, (10)], but with the vacuum Cartan \(\alpha\), gives
\[
 A_N^{(r)}v_{\rm in}
 =(-1)^dNK_{r,T}^d\sum_{a=0}^T
                  \alpha^a V_a^{(r)}\,\mathbf v_a\otimes|T-a\rangle,
                                                                  \tag{4}
\]
where the complete finite scalar sum is
\[
 V_a^{(r)}
   =\sum_{n=a}^T Q^{n(n+r-1)}
                         {T\brack n}_Q{T-a\brack n-a}_Q.        \tag{5}
\]
For verification of the phase, the intermediate coefficient of
\(F^nE^n\) is
\[
 {n\brack a}_Q\alpha^{-(n-a)}
       \frac{f_a f_{T-a}}{f_{T-n}}\,
       Q^{-nT+n(n-1)/2}\frac{f_T}{f_{T-n}}
\]
in the \(\mathbf v_a\otimes|T-a\rangle\) basis. Multiplication by (1) leaves
\(\alpha^a Q^{n(n-1)}(\alpha x)^{-2n}
=\alpha^aQ^{n(n+r-1)}\), proving (4),(5).
This is an actual physical column, not a scalar Casimir evaluation.

Let
\[
 {\cal V}_r(\rho)=\sum_{a=0}^T V_a^{(r)}\rho^a,\qquad
 v_r={\cal V}_r(0).
\]
The original vacuum entry is exactly
\[
                         a_{00}^{(r)}
                 =(-1)^dNK_{r,T}^d v_r.                        \tag{6}
\]
For \(r=2\), [B] proves
\[
 v_2=f_T^2/N,\qquad
 G_2(\rho):={\cal V}_2(\rho)/v_2
      =e^{N\phi(\rho;C)}A(\rho;C)(1+O(N^{-1}))                  \tag{7}
\]
on a fixed disk, with holomorphic relative error and derivatives.
The phase and amplitude used below are exactly these marked functions,
with \(D=\rho\partial_\rho\):
\[
\begin{split}
 CY^2-(1+C-\rho)Y+1-C\rho&=0,\qquad Y(0)=1,\\
 \phi(\rho;C)&=\operatorname{Li}_2(\rho)/c_0
                 +c_0^{-1}\int_0^\rho\log Y(t)\,dt/t,\\
 A(\rho;C)&=(1-\rho)^{-1/2}
      \exp\left(\int_0^\rho Z(t)\,dt/(tY(t))-\tfrac12\log Y(\rho)\right),\\
 Z&=-[CY\,DY+\rho Y-C\rho]/[2CY-(1+C-\rho)].
\end{split}                                                       \tag{8}
\]
Thus \(\phi(0)=0\), \(A(0)=1\), \(\phi'(0)=a:=2/c_0\).
Every estimate below is uniform for \(\sigma_N\in I\).
No \(M\) or \(q\) derivative of these root formulas is taken.

## 2. Exact width recursion with its vacuum source

For \(a<T\), the finite Gaussian identity
\[
 (1-Q^{n-a}){T-a\brack n-a}_Q
       =(1-Q^{T-a}){T-a-1\brack n-a-1}_Q
\]
and (5) give, with \(V_{T+1}^{(r)}=0\),
\[
 V_a^{(r+1)}
       =Q^aV_a^{(r)}-Q^a(1-Q^{T-a})V_{a+1}^{(r)}.               \tag{9}
\]
The boundary case \(a=T\) follows directly from (5). Summing gives the exact
polynomial equation
\[
 \boxed{\quad
 \rho{\cal V}_{r+1}(\rho)
   =(\rho-Q^{-1}){\cal V}_r(Q\rho)
       +Q^T{\cal V}_r(\rho)+(Q^{-1}-Q^T)v_r.
 \quad}                                                        \tag{10}
\]
The numerator on the right vanishes at zero, so its division by
\(\rho\) is literal polynomial division. The last term is the
initialized vacuum source. It must remain, even though the two-tail
seed has a zero-free exponential description.

As a check with no limit, (9) and the exact coefficient [B, (9a)]
give
\[
             v_3=\frac{2(1-Q^{T+1})}{1-Q}\,\frac{f_T^2}{N}.
                                                                  \tag{11}
\]
It is nonzero in the present chamber, although it vanishes at \(T=d\).
The general fixed-width vacuum normalization will follow from the
same forced recursion, rather than from an assumed closed product.

## 3. Microscopic normalization, uniformly through the origin

Set
\[
 b=C^{-1}-1,\qquad p=r-2,\qquad
 W_{r,N}(z)=\frac{{\cal V}_r(z/N)}{v_2N^p}.
\]
Uniformly for \(z\) in any fixed compact complex disk,
\[
 \boxed{\quad
 W_{r,N}(z)
   =b^p\frac{e^{az}-\sum_{j=0}^{p-1}(az)^j/j!}{z^p}
                      +O(N^{-1}).
 \quad}                                                        \tag{12}
\]
For \(p=0\), the empty sum is zero and the quotient is \(e^{az}\).
Every quotient at \(z=0\) is its holomorphic removable value. All
fixed \(z\)-derivatives of the error have the same bound on smaller
disks.

Here is a proof that includes the repeated removals at zero. Equation
(7), evaluated at \(z/N\), gives \(W_{2,N}=e^{az}+O(N^{-1})\) with
fixed derivatives on every fixed disk. On inserting \(\rho=z/N\)
in (10), the exact recurrence is
\[
 zW_{r+1,N}(z)
   =(z/N-Q^{-1})W_{r,N}(Qz)
     +Q^TW_{r,N}(z)+(Q^{-1}-Q^T)W_{r,N}(0).                      \tag{13}
\]
Since \(Q^T=Q^{-1}C^{-1}\), its limiting recurrence is
\[
        zW_{r+1}(z)=b[W_r(z)-W_r(0)].                           \tag{14}
\]
This gives exactly (12). To propagate the error, work on nested
fixed complex disks, finitely many because \(r\) is fixed.
The comparison functions use the exact \(C\) at each \(N\);
no convergence of the discrete parameters \(\sigma_N\) is assumed.
Cauchy bounds give \(W_{r,N}(Qz)-W_{r,N}(z)=O(N^{-1})\)
uniformly on the next smaller disk. The difference between the
numerators in (13),(14) is analytic, vanishes exactly at \(z=0\),
and is \(O(N^{-1})\) on a larger disk. Its quotient by \(z\) is
therefore \(O(N^{-1})\), including at zero, by the maximum principle
or the Cauchy integral for the divided difference. This proves the
induction and all the derivative assertions. No bound with an
uncontrolled factor \(1/|z|\) is used.

At zero, (12) gives the actual normalization
\[
 \boxed{\quad
 \frac{v_r}{v_2}
       =N^p\frac{(ab)^p}{p!}(1+O(N^{-1})).
 \quad}                                                        \tag{15}
\]
The factor \(b\) is uniformly nonzero on \(I\).
Thus \(v_r\), and consequently (6), are nonzero for all sufficiently
large \(N\), uniformly in the stated chamber. In particular
\[
 a_{00}^{(r)}
   =(-1)^dK_{r,T}^d f_T^2
             N^p\frac{(ab)^p}{p!}(1+O(N^{-1})).                 \tag{16}
\]
The exact finite factors \(K_{r,T}^d f_T^2\) have not been replaced
by asymptotic scalars.

Define \(G_r={\cal V}_r/v_r\) for these \(N\). The normalized
microscopic limit is
\[
 \boxed{\quad
 G_r(z/N)=g_p(z)+O(N^{-1}),\qquad
 g_p(z)=p!\sum_{n=0}^\infty\frac{(az)^n}{(n+p)!}.
 \quad}                                                        \tag{17}
\]
For three heads \(p=1\), \(g_1(z)=(e^{az}-1)/(az)\) has a simple
zero at \(z=-2\pi^2\), and at its nonzero integer multiples.
On a small circle about this simple zero, the uniform approximation
(17) and Rouché's theorem give an actual zero of \(G_3(z/N)\) inside
for all large \(N\). Taking smaller circles shows its location is
\[
                       \rho_N=-2\pi^2/N+o(N^{-1}).              \tag{18}
\]
Consequently no fixed disk at zero is zero-free for this actual
three-tail initializer. This is a statement about the actual finite
column, with the original vacuum source in (10).

## 4. Quantitative competing bound and a nonzero sector branch

Shrink the seed disk in (7) once. On it put
\[
       Y_G=e^{c_0D\phi}=\frac{Y}{1-\rho},\qquad
       W(\rho;C)=\frac{C^{-1}-Y(\rho;C)}{\rho}.                  \tag{19}
\]
Its numerator is \(b+O(\rho)\), uniformly; hence it has no zeros
on a sufficiently small punctured disk. It has a pole at zero.
It is not a holomorphic unit on the full disk.

First the following bound retains both the exponential and vacuum:
\[
              |G_r(\rho)|\leq C_r
                         \bigl(1+e^{N\Re\phi(\rho;C)}\bigr)     \tag{20}
\]
uniformly on a fixed smaller closed disk. For \(|\rho|\geq1/N\),
prove by induction that
\[
 |{\cal V}_r(\rho)/v_2|
         \leq C_rN^p(1+e^{N\Re\phi(\rho;C)}).
\]
The seed is (7). In (10), \(|\rho|^{-1}\leq N\), (15) bounds the
vacuum term, and
\(e^{N(\Re\phi(Q\rho)-\Re\phi(\rho))}\) is uniformly bounded by
analyticity of the seed phase and \(|Q-1|=O(N^{-1})\).
This proves the next-width bound, which becomes (20) after (15).
For \(|\rho|\leq1/N\), (17) supplies a uniform bound directly.
This proves (20) on the whole disk, including the origin.
The same argument on slightly larger disks and Cauchy circles of
radius proportional to \(1/N\) gives the corresponding fixed
derivative bounds with at most the expected powers of \(N\).

Let \(\mathcal S\) be any compact set in this punctured disk, with
\(\sigma\in I\), on which \(\Re\phi(\rho;C)\geq\eta>0\).
Then the actual scalar initializer has the stronger asymptotic
\[
 \boxed{\quad
 G_r(\rho)=N^{-p}e^{N\phi(\rho;C)}
       \frac{p!\,A(\rho;C)W(\rho;C)^p}{(ab)^p}
                                      (1+O(N^{-1})).
 \quad}                                                        \tag{21}
\]
Its displayed amplitude is nonzero on \(\mathcal S\).
Such sets exist: \(\phi(\rho)=2\rho/c_0+O(\rho^2)\), so a small
upper-half-plane sector, restricted away from zero, has this property.

To prove (21), first work without the normalization:
\[
       {\cal V}_r/v_2=e^{N\phi}A W^p(1+O(N^{-1})).
\]
It holds for \(r=2\). In (10), the seed phase shift is
\({\cal V}_r(Q\rho)/{\cal V}_r(\rho)=Y_G(1+O(N^{-1}))\)
on slightly enlarged compact sets. The leading multiplier is
\[
          \frac{(\rho-1)Y_G+C^{-1}}{\rho}
                    =\frac{C^{-1}-Y}{\rho}=W.
\]
The retained vacuum has only polynomial size by (15), and is
exponentially smaller than this branch since \(\Re\phi\geq\eta\).
Its contribution and all fixed derivative errors are therefore
controlled. Division by (15) proves (21).
This proof applies to compact subsets of the sector; it does not
claim uniformity as \(\rho\to0\) or as the positive gap closes.

## 5. Entire multivariable boundary and all its branches

Let \(h_a(z_1,\ldots,z_s)\) denote the complete homogeneous polynomial
of degree \(a\). Evaluation of (3),(4) on the original monomial output
row gives the exact source column
\[
\begin{split}
 v_{\mathbf w}A_N^{(r)}v_{\rm in}
       &=a_{00}^{(r)}w_r^T\,{\cal G}_r(z_1,\ldots,z_s),\\
 z_i&=x^{r-i}w_i/w_r,\qquad
 {\cal G}_r(\mathbf z)=\sum_{a=0}^T
                         \frac{V_a^{(r)}}{v_r}h_a(\mathbf z).
\end{split}                                                       \tag{22}
\]
The input is the fixed physical column. If extracted from the
original compact coherent input, its original binomial coefficient
is kept outside (22).

For distinct \(z_i\), the elementary partial fractions of
\(\prod_i(1-z_it)^{-1}\) give
\[
 \boxed{\quad
 {\cal G}_r(\mathbf z)
   =\sum_{i=1}^s
       \frac{z_i^p}{\prod_{j\ne i}(z_i-z_j)}G_r(z_i).
 \quad}                                                        \tag{23}
\]
Equation (22) is the definition at collisions; (23) continues there
by confluent divided differences, not by discarding any summand.
For example on the full diagonal it is
\[
        {\cal G}_r(z,\ldots,z)=
               \frac1{p!}\partial_z^p[z^pG_r(z)].                \tag{24}
\]

Here is a genuine single-branch sector consequence, with all
complements estimated. On a compact configuration set require the
\(z_i\) to be distinct with a fixed separation, and select an index
\(i_*\) such that
\[
 \Re\phi(z_{i_*})\geq\eta,\qquad
 \Re\phi(z_{i_*})\geq
       \max_{j\ne i_*}\{0,\Re\phi(z_j)\}+\eta.                    \tag{25}
\]
All coordinates stay in the small disk; the winning coordinate is
automatically bounded away from zero. Its coefficient in (23) is
nonzero and bounded away from zero on the compact set.
Equations (20),(21) now give the actual estimate
\[
\begin{split}
 {\cal G}_r(\mathbf z)
   ={}&N^{-p}e^{N\phi(z_{i_*};C)}
     \frac{z_{i_*}^p}{\prod_{j\ne i_*}(z_{i_*}-z_j)}
     \frac{p!\,A(z_{i_*};C)W(z_{i_*};C)^p}{(ab)^p}\\
     &\hspace{35mm}\cdot(1+O(N^{-1})).
\end{split}                                                       \tag{26}
\]
Every losing term, including a coordinate at zero, is bounded by
(20); relative to the displayed term it is at most
\(C N^p e^{-N\eta}\). Thus (26) is not a selection based solely on
formal phases. It estimates the original finite boundary sum.
The exact normalization and monomial in (22) remain outside it.

At phase ties or collisions the sum (23), or its confluent version,
must instead remain. There is a uniform microscopic formula making
this explicit. On every fixed compact \(\mathbf z\)-set,
\[
 {\cal G}_r(z_1/N,\ldots,z_s/N)
   =p!a^{-p}\sum_{i=1}^s
                \frac{e^{az_i}}{\prod_{j\ne i}(z_i-z_j)}
                                      +O(N^{-1}),               \tag{27}
\]
with the entire divided-difference continuation at collisions.
Indeed insert (17) in (23); the polynomial of degree \(p-1\)
subtracted from the exponential has zero divided difference.
Uniformity through collisions follows from the fixed-order Cauchy
integral for divided differences on a surrounding circle and (17).
The same argument proves fixed derivatives. On the full diagonal
the right side is \(e^{az}\). For \(r=3\) with the second coordinate
zero it is exactly the profile in (17),(18). This retains both
nonzero diagonal behavior and genuine nearby interference zeros.

## 6. Scope and complete directs

This is an actual arbitrary-fixed-width initialization result:
(4),(10),(22) preserve all physical coefficients and endpoint support;
(15) pays the vacuum normalization; (20) controls every competing
boundary term; (21),(26) give nonzero local branches where the stated
quantitative gaps hold. The microscopic and confluent rows are retained
when these hypotheses fail. No replacement positive packet is used.

The universal operator also commutes with its consecutive partial
Casimirs: each commutes with the total \(E,F,K\) by the ordered
coproduct and centrality on its own interval, hence with (1).
This note does not solve their multi-variable kernel
equations. In particular it makes no higher-width full-kernel,
meridian-normal, inverse-frame, geometric-chart, relative-cycle or
volume assertion. All exterior factors in [G]'s original opposite
kernel remain.

Complete proof directs:

- **G:** [research_opposite_kernel_forced_cyclic_normalization.md](research_opposite_kernel_forced_cyclic_normalization.md),
  489 lines, SHA256
  42e6d6c3a5039859c241a2832de56301eff49d749db86d67868f3534c89aaaaa.
- **B:** [research_actual_gauss_first_column_unit.md](research_actual_gauss_first_column_unit.md),
  415 lines, SHA256
  ebe3b496a739d1734738e4b663c7a7fd6713e44549b72ee2e93ae90314a15047.

Both complete directs were read nontruncated in the active author
sequence. The new width recursion, microscopic removal, sector estimates
and divided-difference lift are proved inline. Only written mathematics
and text/hash operations are used.

Author freeze protocol: the entire matching final was reread
nontruncated; both complete direct reads were explicitly retained fresh
and unchanged from this active author sequence. Every used implication
was checked, and all three hashes were renewed. Independent matching
review and parent adoption remain separate.

