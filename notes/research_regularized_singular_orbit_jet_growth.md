# Orbit jets across the retained complete-meridian divisor

Research deduction, 6 November 2026.

The regular-arc hypothesis in the
[orbit-jet theorem](research_regularized_orbit_jet_growth.md) is not
automatic for the actual normal operator. This note gives a singular-arc
extension with an explicit vanishing rate cost. It applies, in particular,
to the already proved actual figure-eight operator, whose two classical
end coefficients vanish at the complete meridian. The operator and its
whole leading germs are retained throughout.

The general extension does not identify the complete-value rate with
the joint growth envelope. The figure-eight calibration below also uses
its independently proved actual microscopic profile. No meridian jets
are replaced by the bounded quantum-parameter jets of fixed colors.

## 1. What the actual pointing and Weyl symmetry require

Use
\[
 q_N=e^{\pi i/N},\quad Q_N=q_N^2,\quad
 T_Nh(Y)=h(Q_NY),\quad
 v_N(Y)=(Y-1)F_N(Y).
 \tag{1}
\]
The actual reduced period satisfies
\(F_N(Q_N^j)=C_j(q_N)\) for \(1\le j<N\),
\(F_N(1)=C_N(q_N)=K_N\), and \(C_j(1)=1\).
Let
\[
 B(q,Y,T)=\sum_{i=0}^d b_i(q,Y)T^i,\qquad
 b_i\in\mathbb C[q^{\pm1},Y^{\pm1}],
 \qquad B(q_N,Y,T_N)v_N=0
 \tag{2}
\]
be a specified actual normal operator, with its recorded normalization.
All orders and coefficient supports here are independent of \(N\).

Cross-level polynomial rigidity gives the exact generic identity
\[
 \sum_{i=0}^d b_i(q,q^{2j})(q^{2(j+i)}-1)C_{j+i}(q)=0
                         \qquad(j\ge1).
 \tag{3}
\]
This is the same identity used in
[bounded normal-color transfer](bounded_normal_color_transfer.md),
Section 1. Write \(q=e^h\). The coefficient of \(h\) in (3), using
\(C_{j+i}(1)=1\), is
\[
 \sum_{i=0}^d b_i(1,1)(j+i)=0\qquad(j\ge1).
 \tag{4}
\]
Thus
\[
 B_{\rm cl}(1,1)=0,\qquad
 \partial_LB_{\rm cl}(1,1)=0,\qquad
 B_{\rm cl}(Y,L)=\sum_i b_i(1,Y)L^i.
 \tag{5}
\]
If \(B_{\rm cl}(1,L)\) is not identically zero, it has a double
root at \(L=1\). In particular a classically regular order-one
normal equation is impossible. This conclusion uses the actual generic
color pointing, not just arbitrary values on each root orbit.

For the primitive minimal normal operator, the proved
[Weyl reciprocity](actual_weyl_descent.md), Section 3, says
\[
 B_{\rm cl}(Y,L)
   =-\sigma Y^{m-1}L^d B_{\rm cl}(Y^{-1},L^{-1}),
 \qquad \sigma\in\{1,-1\},\quad m\in\mathbb Z.
 \tag{6}
\]
Consequently \(b_0(1,1)=-\sigma b_d(1,1)\). Neither (5) nor
(6) forces these two coefficients to vanish: a nonzero polynomial
with a double root at \(1\) can have nonzero end coefficients.
This is compatibility of the necessary algebraic constraints, not an
existence assertion for a positive-growth knot with a regular minimal
normal operator.

The positive-growth obstruction in
[the peripheral normal-period theorem](peripheral_normal_period.md),
Section 2, concerns the reduced operator \(P=B(Y-1)\). Its coefficient
of \(T^i\) is
\[
                  b_i(q,Y)(q^{2i}Y-1).
 \tag{7}
\]
Every complete column of \(P\) therefore vanishes exactly, including
when \(b_0(1,1)b_d(1,1)\ne0\). That argument cannot be reapplied to
force an additional divisor of \(B\).
Conversely, the manufactured regular-\(B\) families in Section 8 of
that note do not establish actual compatibility: they violate the
coherent identities \(C_N(q_N)=K_N\). No such family is substituted
for the fixed source here.

## 2. A singular-arc observation theorem

Let \(R_N\) be Laurent polynomials with
\[
 \operatorname{supp}R_N\subset[-AN,AN],\qquad
 \|R_N\|_{|Y|=1}\le e^{GN}
 \tag{8}
\]
eventually, where \(A\ge1\) is a fixed integer and \(G>0\).
Suppose the exact equation is
\[
 \sum_{i=0}^d b_i(q_N,Y)R_N(Q_N^iY)=\beta_N(Y),
 \tag{9}
\]
where \(\beta_N\) has fixed Laurent support and polynomially bounded
coefficients. Require:

1. \(b_0(1,Y)\) and \(b_d(1,Y)\) are nonzero Laurent polynomials.
2. Near \((q,Y)=(1,1)\), each of their zero divisors over \(Y=1\)
   factors into finitely many analytic branches
   \(Y=\lambda_r(q)\), with \(\lambda_r(1)=1\), counted with
   multiplicity, times a holomorphic nonvanishing factor.

The second condition is exactly the local analytic-divisor hypothesis
used in [the tempered growth theorem](tempered_a_growth_bound.md),
Section 2. It is automatic for simple classical roots and for products
of monomial binomials. No ramified branch is treated as analytic.
Choose a sufficiently small fixed arc about \(1\) containing no other
classical end-coefficient zero.

Define \(\mathscr D_N=N^{-1}Y\partial_Y\), \(U_0\), \(\mathcal J_{N,K}\)
and \(a_K\) as in the orbit-jet theorem:
\[
 \begin{split}
 U_0&=\lim_{\delta\downarrow0}\limsup_N
       N^{-1}\log\sup_{|z|<\delta}|R_N(e^z)|,\\
 \mathcal J_{N,K}
   &=1+\max_{\substack{0\le i<d\\0\le r<K}}
                         |\mathscr D_N^rR_N(Q_N^i)|,\qquad
 a_K=\limsup_N N^{-1}\log\mathcal J_{N,K}.
 \end{split}
 \tag{10}
\]
Let \(D_\pm\) be the Laurent \(Y\)-exponent spans of \(b_0,b_d\),
respectively, and put \(D_*=D_-+D_+\).

**Theorem 1.** There are constants \(C>0\) and \(\alpha_*>0\),
independent of the fixed jet order, such that every
\(0<\alpha<\alpha_*\) admits a finite integer \(K_\alpha\) with
\[
 0\le a_{K_\alpha}\le\max(0,U_0)
 \le a_{K_\alpha}
        +C\alpha\bigl(1+|\log\alpha|\bigr).
 \tag{11}
\]
In particular
\[
                       \sup_{K\ge1}a_K=\max(0,U_0).
 \tag{12}
\]
In the proof, crossing all exact end-coefficient zeros costs at most
\(D_*\) extra initial meridian-jet orders. This bound concerns the
whole leading germ, including its zeros. It does not invert a zero
specialized coefficient or delete a common classical meridian factor.

### 2.1. The whole local leading germ

Use a common scaled logarithmic coordinate along an orbit segment:
\(Y=Q_N^j e^{s/N}\). The Taylor coefficients of \(R_N\) in \(s\)
are \(\mathscr D_N^rR_N(Q_N^j)/r!\).
For either end coefficient \(p=b_0\) or \(p=b_d\), set
\[
 p_{N,j}(s)=p(q_N,Q_N^j e^{s/N}),\quad
 m_{N,j}=\operatorname{ord}_{s=0}p_{N,j},\quad
 \eta_{N,j}=[s^{m_{N,j}}]p_{N,j}.
 \tag{13}
\]
Each orbit point occurs at most once on the small segment. The
sum of \(m_{N,j}\) is at most the \(Y\)-span of \(p\), by root
multiplicity counting. This is the meridian budget in
[bounded meridian jets](bounded_meridian_jets.md), not the different
quantum-parameter budget of the pointed Gram theorem.

The analytic branches move by \(O(N^{-1})\). Choose a fixed integer
\(J\) large enough to dominate all these displacements in grid units.
If \(J\le |j|\le\alpha N/(2\pi)+O(1)\), local factorization gives
\[
 |p(q_N,Q_N^j)|\ge c(|j|/N)^\mu ,
 \tag{14}
\]
where \(\mu\) is the multiplicity of \(p(1,Y)\) at \(1\).
There are no exact zeros at these points.

For the finitely many \(|j|<J\), every fixed Taylor coefficient in
(13) is \(N^{-r}\) times a fixed analytic germ in \(q_N\):
monomial \(c q^aY^b\) contributes
\(c q_N^{a+2bj}b^r/(r!N^r)\).
After excluding finitely many levels, its first nonzero coefficient
therefore has modulus bounded below by a fixed power of \(N^{-1}\).
The possible first nonzero orders are bounded by the fixed \(Y\)-span.
These statements are uniform over this finite set of offsets.

For any segment of length at most \(\alpha N/(2\pi)+O(1)\),
(14) and the finite near-zero analysis give
\[
 \prod_j|\eta_{N,j}|^{-1}
 \le N^{C_0}\exp\!\left[
       C_1N\alpha(1+|\log\alpha|)\right].
 \tag{15}
\]
Indeed
\(\sum_{j=J}^n\log(N/j)\le n\log(N/n)+n+O(\log N)\).
The same estimate holds on the negative arc and for both end
coefficients. Take \(\alpha_*\) small enough that this upper bound
is increasing for the segment lengths in question.

There is also a polynomial bound, for each fixed \(K\), on the first
\(K\) coefficients of
\[
 \left(\prod_j p_{N,j}(s)\right)
       \bigg/\left(s^{\sum_jm_{N,j}}\prod_j\eta_{N,j}\right)
 \quad\hbox{and its reciprocal}.
 \tag{16}
\]
For the bounded near-zero offsets this follows from the same fixed
analytic germs. Elsewhere (14), bounded coefficient derivatives and
the factor \(N^{-r}\) bound each fixed normalized coefficient by a
power of \(N\). A product of \(O(N)\) such unit series has each fixed
coefficient polynomially bounded, as does its inverse. No estimate
on an arbitrarily high, \(N\)-dependent Taylor order is used.

### 2.2. Transfer and localization

Write the companion recurrence with its scalar leading coefficient
on the left, and multiply the numerator matrices before taking any
Taylor coefficient. An affine equation causes no additional issue:
choose \(N^p\) dominating the coefficients of \(\beta_N\), adjoin the
constant coordinate \(N^p\), and use \(\beta_N/N^p\) in the last
column. The resulting numerator matrices are uniformly bounded.
Their fixed Taylor lifts have diagonal block equal to the value
matrix and off-diagonal blocks \(O_K(N^{-1})\).
Consequently their product along the segment has norm at most
\[
                  (M+O_K(N^{-1}))^{O(\alpha N)},
 \tag{17}
\]
with \(M\ge1\) independent of the fixed jet order \(K\).
The bound on each derivative uses only fixed Laurent coefficient
supports, including the fixed support of \(\beta_N\).

The actual solution is holomorphic. Divide its whole numerator
series by the whole leading series, using (16). To obtain output
jets through order \(K-1\) requires numerator and initial jets only
through order \(K-1+\sum_jm_{N,j}\). Combining (15)--(17), forward
and backward propagation gives
\[
 \max_{\substack{|\arg Q_N^j|\le\alpha\\0\le r<K}}
 |\mathscr D_N^rR_N(Q_N^j)|
 \le C_KN^{p_K}
   e^{CN\alpha(1+|\log\alpha|)}\mathcal J_{N,K+D_*}.
 \tag{18}
\]
All finite negative-power compatibility conditions are supplied by
the actual regular solution. They are not extra initial choices.
The constant \(C\) is independent of \(K\); polynomial constants
and the starting level may depend on \(K\).

Now use precisely the full-circle Hermite sampling and localization
proof in Sections 2 and 4 of the orbit-jet theorem. Namely take
\(w(Y)=(2+Y+Y^{-1})/4\), choose a fixed integer \(L\) with
\[
 G+L\log\cos^2(\alpha/2)<-2,
 \tag{19}
\]
and apply its Hermite bound to \(w^{LN}R_N\), of Laurent support
in \([-(A+L)N,(A+L)N]\). It needs \(2(A+L)+1\) orbit jets.
Equation (18) bounds those jets by the initial block with
\(K_\alpha=2(A+L)+1+D_*\). Outside the arc the localization has
strictly negative rate. Near \(z=0\), division by the localization
costs only \(O(L|z|^2)\) in normalized logarithmic rate. Let
\(N\to\infty\), then the complex neighborhood shrink, with
\(\alpha,L,K_\alpha\) fixed. This proves the last inequality in
(11). Cauchy's estimate at the fixed number of coalescing orbit
points gives \(a_K\le\max(0,U_0)\) for every fixed \(K\).
Letting \(\alpha\downarrow0\) proves (12).

## 3. A concrete application with a vanishing classical factor

The actual figure-eight Laurent state is identified in
[the whole-source theorem](figure_eight_whole_source_identity.md)
with the finite product sum used in
[the peripheral normal-period note](peripheral_normal_period.md),
Section 9. Keep exactly its homogeneous operator \(P\), after the
recorded common coefficient factor has been removed, and put
\(P=B(Y-1)\).
Its displayed finite certificate gives, with \(Q=q^2\),
\[
 \begin{split}
 b_0(q,Y)&=-Q^3Y^2(Q^2Y+1)(Q^5Y^2-1),\\
 b_3(q,Y)&=\phantom{-}Q^4Y^2(QY+1)(QY^2-1).
 \end{split}
 \tag{20}
\]
These expressions follow directly from the extreme coefficients:
before removing the common factor
\(Q^3Y(Q^3Y^2-1)^2\), they are
\(-D(Q^2Y)c_-(QY)\) and \(D(QY)c_+(Q^2Y)\);
then divide respectively by \(Y-1\) and \(Q^3Y-1\), as dictated
by the exact right multiplication \(P=B(Y-1)\).
This uses the existing certificate algebra, not a new source run.

Both classical end coefficients vanish at \(Y=1\):
\[
 b_0(1,Y)=-Y^2(Y+1)(Y^2-1),\qquad
 b_3(1,Y)=Y^2(Y+1)(Y^2-1).
 \tag{21}
\]
Thus the regular-arc hypothesis fails for this specified actual
normal operator, even though its original complete period has
proved positive exponential growth.
Its near-\(1\) divisor branches, however, are exactly
\[
                        Y=q^{-5},\qquad Y=q^{-1}.
 \tag{22}
\]
They are analytic and are never root-orbit points \(Q_N^j\) for
large \(N\): their exponents are odd half-steps. All other roots
of the two end coefficients lie near \(-1\), outside a fixed small
complete-meridian arc. Hence Theorem 1 applies; on that arc its
exact pole budget can even be taken to be zero.

The actual regularized remainder \(R_N\), rather than a manufactured
root solution, satisfies (8)--(9) by
[the actual growth-characteristic theorem](research_regularized_period_growth_characteristics.md),
Sections 1--2, and the degree proof in the orbit-jet theorem.
It follows that
\[
 \sup_{K\ge1}\limsup_N\frac1N\log\!\left(
 1+\max_{\substack{0\le i<3\\0\le r<K}}
                  |\mathscr D_N^rR_N(Q_N^i)|\right)
             =\max(0,U_0).
 \tag{23}
\]
The common classical meridian factor has not been deleted. The
finite number of nearby points, the accuracy-dependent finite jet
order, and the limsup remain exactly as stated.

**Corollary 2 (actual joint growth at completeness).** For the actual
figure-eight regularized remainder,
\[
 \lim_{\delta\downarrow0}\limsup_{N\to\infty}
       \frac1N\log\sup_{|z|<\delta}|R_N(e^z)|
   =\kappa_8,\qquad
 \kappa_8=\frac{\operatorname{Vol}(S^3\setminus4_1)}{2\pi}.
 \tag{24}
\]
This calibrates the whole complex joint upper rate. It uses, rather
than reproves, the already established complete-value volume
asymptotic and microscopic source profile.

Indeed, the [paired-factor meridian theorem](actual_paired_factor_meridian_profile.md),
Section 3, equations (13)--(14), retains exactly this ordinary-color
subtraction and proves
\[
 \begin{split}
 R_N(e^{\zeta/N})
   &=\frac{K_N}{N}e^{-(N-1)\zeta/(2N)}\rho_N(\zeta),\\
 \rho_N(\zeta)&=1+O_R(N^{-1}),\qquad
             \frac1N\log K_N\longrightarrow\kappa_8>0 .
 \end{split}
 \tag{25}
\]
The first two assertions hold on each fixed complex \(\zeta\)-disk
with every fixed derivative, including the ordinary-color resonances.
The last assertion is the original positive complete-value theorem.
The variable \(\zeta\) in (25) is microscopic; the variable \(z\)
in (24) is unscaled and its disk shrinks only after the level limit.

Differentiation in \(\zeta\) is exactly \(\mathscr D_N\) on the
composed function. At \(\zeta=2\pi i j\), for fixed integers
\(j,r\ge0\), (25) gives
\[
 \mathscr D_N^r R_N(Q_N^j)
  =\frac{K_N}{N}(-1)^j
       \left[\left(-\frac12\right)^r+O_{j,r}(N^{-1})\right].
 \tag{26}
\]
Here the centering phase is
\(e^{-(N-1)\pi i j/N}=(-1)^j e^{\pi i j/N}\);
it has not been omitted from the rate calculation.
Consequently every fixed nonempty jet block in (23) has
\(a_K=\kappa_8\). Applying (23) proves (24).
The microscopic theorem by itself makes no assertion on a fixed
complex meridian neighborhood; the singular-arc transfer supplies
the passage to the joint rate. Equation (24) is not a pointwise
asymptotic at every meridian of such a fixed neighborhood.

## 4. Remaining operator and source distinctions

For a general actual primitive normal operator, neither classical
end-degree preservation nor the local analytic-divisor hypothesis
is established by the existing construction. A common factor of
the classical coefficient list can occur without being a common
factor of the quantum list. Dividing that classical factor does not
produce an exact equation for \(R_N\).

The finite meridian pole budget alone is not a logarithmic norm
estimate: it counts exact zeros but does not control arbitrarily
small nonzero end coefficients. The analytic-divisor assumption is
used precisely to locate all dangerous steps within \(O(N^{-1})\)
of the complete meridian and to bound their nonzero leading germs
by powers of \(N\). A ramified divisor or a classical end-degree
drop requires an additional argument; neither is silently covered.

Finally, the bounded initial jets in
[the pointed Gram theorem](pointed_a_gram_period.md) and
[the tempered growth theorem](tempered_a_growth_bound.md) differentiate
the fixed colors while \(q\) and their color argument vary together.
The observations in (10) and (23) differentiate \(Y\) with \(q=q_N\)
fixed. The original state identities do not equate these two kinds
of derivatives. Weyl symmetry also does not supply that equality.
The new theorem therefore retains the finite meridian observations;
it gives no bound on them from ordinary-color values alone and no
zero-jet or all-level complete-value conclusion.

There is now a function-level alternative in
[the fixed microscopic-disk theorem](research_regularized_microscopic_disk_growth.md).
It removes the analytic-divisor hypothesis by transferring on a
common microscopic circle before taking any derivatives. Under the
same classically nonzero end-polynomial condition, one fixed disk
norm has exactly the positive joint growth rate. Its observation is
a whole function norm, rather than the finite jet block of Theorem 1.
It still needs a source comparison with the single complete value.
