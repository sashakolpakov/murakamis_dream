# Alternating physical-row linearization and odd-turn quadratic phases

Private written proof, 17 November 2026.

The ordinary product of two original physical rows has strictly
alternating linearization coefficients throughout its full triangle
support, provided its degree stays in the physical-row range.
A finite positive recursion proves the signs and computes every
coefficient. An odd signed turn removes precisely the alternating
signs, retaining a sum with positive amplitudes and the original
quadratic phases.

Above this degree range, an expansion in physical value rows alone
is impossible. The original normal rows supply the missing degrees
and have the retained Jordan action. No cancellation or lower bound
for the resulting quadratic sum is inferred.

## 1. Original rows and monic normalization

Use
\[
 N\ge2,\quad D=N-1,\quad J=\lfloor D/2\rfloor,\quad
 \theta=\pi/N,\quad q=e^{i\theta},\quad
 \eta=(-1)^D,\quad \kappa=q^{D^2/2},
\]
\[
 s_r=2\sin(r\theta),\quad S_r=\prod_{a=1}^r s_a,\quad S_0=1,
 \quad c_r=2\cos((2r+1)\theta),
\]
\[
 P_N(Z)=2T_N(Z/2)+2,\quad
 e_r(Z)=S_r^{-2}\prod_{a<r}(c_a-Z),\quad
 K_N(w,Z)=\sum_{r=0}^{D}e_r(w)e_r(Z).
 \tag{1}
\]
All canonical operators are in the original full algebra
\(\mathcal A_N=\mathbb C[Z]/(P_N)\). Its physical turn satisfies
\(Te_r=e_{D-r}\), and
\[
                  V_n=\kappa^nTR^{-n}T,\qquad n\in\mathbb Z.
 \tag{2}
\]
Write
\[
              F_j(Z)=K_N(c_j,Z),\qquad 0\le j\le J.
 \tag{3}
\]
These polynomials have degree exactly \(j\), with \(F_0=1\).
Their original recurrence, for \(0\le r<J\), is
\[
 A_rF_{r+1}=(c_0+A_r+C_r-Z)F_r-C_rF_{r-1},
 \tag{4}
\]
\[
 A_r=\frac{s_{r+1}^4}{s_{2r+1}s_{2r+2}},\qquad
 C_r=\frac{s_r^4}{s_{2r}s_{2r+1}}\ (r\ge1),\qquad C_0=0.
 \tag{5}
\]
The term containing \(F_{-1}\) is absent. Every displayed
denominator in this range is nonzero, and \(A_r>0\),
\(C_r>0\) when \(r\ge1\).

Put
\[
 H_0=1,\qquad H_j=\prod_{r=0}^{j-1}A_r
                    =\frac{S_j^4}{S_{2j}}>0,\qquad
 p_j=(-1)^jH_jF_j .
 \tag{6}
\]
The factorial formula follows by multiplying (5); \(2j<N\)
for all \(j\le J\). Thus \(p_j\) is monic and
\[
 p_0=1,\quad p_1=Z-b_0,\quad
 p_{r+1}=(Z-b_r)p_r-a_rp_{r-1},
 \tag{7}
\]
Only indices at most \(J\) are used; the \(p_1\) identity
applies when \(J\ge1\).
\[
 b_r=c_0+A_r+C_r,\qquad
 a_r=A_{r-1}C_r\ (r\ge1),\qquad a_0=0 .
 \tag{8}
\]

## 2. Strict monotonicity before the physical fold

Only \(b_0,\ldots,b_{J-1}\) and \(a_0,\ldots,a_{J-1}\)
will be used. When \(N\le4\), \(J\le1\), so all products in
the theorem below have a constant factor. For the nontrivial
range assume \(N\ge5\).

**Lemma 1.** The two sequences in (8) are strictly increasing
over their stated ranges.

**Proof.** The sine addition formulas give
\[
 b_r=\frac8{c_0+c_r}
     =\frac2{\cos(r\theta)\cos((r+1)\theta)} .
 \tag{9}
\]
For example, with \(u=r\theta\), use
\[
 \frac{\sin^3(u+\theta)}{\cos(u+\theta)}
   +\frac{\sin^3u}{\cos u}
 =\tan(u+\theta)+\tan u
       -\tfrac12\{\sin(2u+2\theta)+\sin2u\}
\]
in (5). This gives \(A_r+C_r=8/(c_0+c_r)-c_0\);
at \(r=0\), the expression has the stated removable value.
The denominators in (9) are positive before the fold, and
\(c_r\) strictly decreases. Hence \(b_r\) strictly increases.

For \(r\ge1\), exactly
\[
 a_r=\frac{s_r^8}{s_{2r-1}s_{2r}^2s_{2r+1}}
     =\frac{(1-x_r)^3}{(1+x_r)(d-x_r^2)},\qquad
 x_r=\cos(2r\theta),\quad d=\cos^2\theta .
 \tag{10}
\]
For \(1\le r\le J-1\),
\[
          -\cos2\theta\le x_r\le\cos2\theta<\cos\theta.
 \tag{11}
\]
Here \(\cos2\theta>0\). The denominators in (10) are
positive on this interval. The logarithmic derivative of its
right-hand function \(a(x)\) is
\[
 \frac{a'(x)}{a(x)}
 =\frac{2\{2x^2+(1-d)x-2d\}}
              {(1-x^2)(d-x^2)}.
 \tag{12}
\]
The numerator's quadratic is convex. At the two ends
\(x=\pm(2d-1)=\pm\cos2\theta\), its values are respectively
\[
                  (6d-1)(d-1),\qquad (10d-3)(d-1).
 \tag{13}
\]
Both are negative because \(N\ge5\) gives \(1/2<d<1\).
Convexity makes the numerator strictly negative on (11).
Since \(x_r\) strictly decreases with \(r\), \(a_r\)
strictly increases. Finally \(a_0=0<a_1\) whenever the
latter is required. This proves the lemma. \(\square\)

No recurrence at or beyond the singular physical end has
been imposed in this argument.

## 3. A finite positive product recursion

We give the algebraic mechanism explicitly. It applies to the
monic recurrence (7), with no orthogonality or literature
linearization theorem as an additional premise.

For \(1\le m\le n\), \(m+n\le J\), define
\[
                    D_{m,n}=p_mp_n-p_{m-1}p_{n+1}.
 \tag{14}
\]
The recurrence gives, for \(m\ge2\),
\[
 \begin{split}
 D_{m,n}={}&(b_n-b_{m-1})p_{m-1}p_n
       +(a_n-a_{m-1})p_{m-1}p_{n-1}\\
       &+a_{m-1}D_{m-1,n-1},
 \end{split}
 \tag{15}
\]
with the exact starting identity
\[
                 D_{1,n}=(b_n-b_0)p_n+a_np_{n-1}.
 \tag{16}
\]
To verify (15), expand \(p_m\) and \(p_{n+1}\) by (7).
The \(Z\)-terms cancel. Add and subtract
\(a_{m-1}p_{m-1}p_{n-1}\); what remains is precisely
the last difference in (15).

Let \(g_{m,n;\ell}\) be the coefficients in
\[
                         p_mp_n=\sum_\ell g_{m,n;\ell}p_\ell .
 \tag{17}
\]
The following is one explicit finite formula by recursion:
\[
 g_{0,n;\ell}=\mathbf1_{\ell=n},
 \tag{18}
\]
\[
 \begin{split}
 g_{m,n;\ell}={}&g_{m-1,n+1;\ell}\\
 &+\sum_{r=0}^{m-1}
       \left(\prod_{h=1}^{r}a_{m-h}\right)
       \bigl\{
        (b_{n-r}-b_{m-r-1})g_{m-r-1,n-r;\ell}\\
 &\hspace{42mm}
       +(a_{n-r}-a_{m-r-1})g_{m-r-1,n-r-1;\ell}
       \bigr\},
                  \qquad 1\le m\le n,\quad m+n\le J .
 \end{split}
 \tag{19}
\]
An empty product is one; exchange \(m,n\) if necessary.
Every coefficient on the right has smaller first index and
uses valid physical indices. Thus (18)--(19) is a terminating
finite prescription. Substituting the explicit sine coefficients
(8)--(10) gives the exact rational coefficient at every level.
Unrolling the recursion is a finite sum of products of its
positive weights. It introduces no singular factorial or
infinite series.

**Proposition 2.** The coefficients in (17) obey
\[
 g_{m,n;\ell}>0\quad\text{if }|m-n|\le\ell\le m+n,
 \qquad g_{m,n;\ell}=0\quad\text{otherwise},
 \tag{20}
\]
including the one-term convention when one index is zero.

**Proof.** Unroll (15) down to (16) and add
\(p_{m-1}p_{n+1}\). This proves the polynomial identity
(19), hence its coefficients. Induct on \(m\), taking \(m\le n\).
Lemma 1 makes every difference in braces strictly positive:
its larger index exceeds its smaller index by \(n-m+1\).
All other multipliers are positive.

The first term in (19) has no support below \(n-m+2\).
The first and second products in each brace have no support
below \(n-m+1\) and \(n-m\), respectively, by induction.
None has degree above \(m+n\). Hence no coefficient outside
the asserted range occurs.

For strict positivity inside that range, the \(r=0\) first
product has positive coefficients on
\([n-m+1,n+m-1]\); the second has positive coefficients
on \([n-m,n+m-2]\). For \(m=1\) these are the individual
indices \(n\) and \(n-1\). Together they cover the entire
range except its top index \(n+m\), whose coefficient is
one because the product is monic, also supplied by the
first term in (19). This proves (20). \(\square\)

## 4. Alternating signs and the original odd turn

**Theorem 3.** For all original physical indices \(j,k\) with
\(j+k\le J\), exactly as ordinary polynomials,
\[
 \boxed{\quad
 F_jF_k=\sum_{\ell=|j-k|}^{j+k}
           (-1)^{j+k-\ell}\mathsf A_{jk\ell,N}F_\ell,\qquad
 \mathsf A_{jk\ell,N}
       =\frac{H_\ell}{H_jH_k}g_{j,k;\ell}>0 .
 \quad}
 \tag{21}
\]
The factorial normalization is \(H_r=S_r^4/S_{2r}\),
and (18)--(19) specifies every coefficient by a finite
positive recursion. The formulas hold at both parities.
For \(j=k=1\) they recover
\[
 \mathsf A_{112}=\frac{c_0^4}{(c_0^2-1)(c_0^2-2)},\quad
 \mathsf A_{111}=\frac4{c_0^2-2},\quad
 \mathsf A_{110}=\frac1{c_0^2-1}.
 \tag{22}
\]

**Proof.** Substitute \(p_r=(-1)^rH_rF_r\) in (17)
and apply Proposition 2. The special case follows from
(8)--(10), or the first recurrence step (16).
The degree is at most \(J<N\), so no canonical reduction
or hidden quotient equality is used. \(\square\)

For completeness, the exact physical-row turn law is
\[
                  V_nF_\ell=(-1)^{n\ell}
                              q^{-n\ell(\ell+1)}F_\ell .
 \tag{23}
\]
Indeed
\[
 TF_\ell=\delta_{c_\ell}
        =\frac{P_N(Z)}{\eta N^2(Z-c_\ell)}
 \tag{24}
\]
and multiplication by any polynomial \(r\) on this vector
is \(r(c_\ell)\). Thus \(V_nF_\ell\) is a scalar multiple
of \(F_\ell\). The full triangular matrix of the original
unit turn with sign \(\sigma\in\{1,-1\}\) has degree-\(\ell\) diagonal
\((-1)^\ell q^{-\sigma\ell(\ell+1)}\); comparison of leading
coefficients and then integer powers proves (23).
Divisibility by the full relation in (24) retains every normal.

Combining (21) and (23), for every odd signed integer \(n\),
\[
 \boxed{\quad
 V_n(F_jF_k)=(-1)^{j+k}
       \sum_{\ell=|j-k|}^{j+k}
       \mathsf A_{jk\ell,N}\,
                  q^{-n\ell(\ell+1)}F_\ell .
 \quad}
 \tag{25}
\]
For even \(n\), the summand also has the sign \((-1)^\ell\).
All quadratic phases in (25) are original. Positive amplitudes
are not a declaration that their coherent sum is positive,
zero-free, or of a specified geometric action.

## 5. The high-degree boundary and its full normal channels

For physical \(j,k\le J\), always \(j+k\le2J\le D\).
Consequently, if \(j+k>J\), the product has degree \(j+k\)
even in its canonical representative. Every linear combination
of the physical rows \(F_0,\ldots,F_J\) has degree at most \(J\).
An \(F\)-only linearization is therefore impossible in this
range. Canonical reduction cannot repair it.

At each double physical node retain
\[
                         G_j(Z)=\partial_wK_N(c_j,Z).
 \tag{26}
\]
Its degree is exactly \(D-j\). In fact \(e_k'(c_j)=0\)
once \(k>D-j\), because both occurrences \(j,D-j\) of the
node are then present in the Newton product. At \(k=D-j\)
only the first occurrence is present, so its derivative is
nonzero. Therefore
\[
        \{F_j:0\le j\le J\}
        \ \cup\ \{G_j:c_j\text{ is double}\}
 \tag{27}
\]
has exactly one nonzero polynomial of each degree \(0,\ldots,D\)
and is a basis of the full algebra. At odd levels the final
simple row has no added \(G_j\).

Its retained signed-turn action is
\[
 \boxed{\quad
 V_nG_j=\lambda_{n,j}G_j
          +\kappa^n(R^{-n})'(c_j)F_j,\qquad
 \lambda_{n,j}=(-1)^{nj}q^{-nj(j+1)} ,
 \quad}
 \tag{28}
\]
where the prime is the original spectral first normal.
To verify it, differentiate the ordinary reproducer before
specializing a double node. Since \(P_N(c_j)=P_N'(c_j)=0\),
\[
 TG_j=\frac{P_N(Z)}{\eta N^2(Z-c_j)^2}.
 \tag{29}
\]
Multiplication by \(r\) on (29) gives \(r(c_j)\) times
(29), plus \(r'(c_j)\delta_{c_j}\), modulo the full relation.
Apply \(T\), with \(r=R^{-n}\), to obtain (28).
The original normal is not replaced by a derivative of a
chosen off-grid phase.

Equations (27)--(29) locate the additional channels required
above the range of Theorem 3. No sign assertion for their
product coefficients is made here. In particular an odd turn
there must retain its triangular normal coupling, not merely
the scalar phase in (23).

## Scope and direct sources

The theorem is a general local composition identity for actual
physical rows, with unrestricted indices in its stated low-degree
range. It supplies a larger coherent class than phase-positive
Laurent polynomials: the odd-turn expression (25) has positive
amplitudes with an explicit quadratic phase. Bounding that sum
after further original products, turns and closing remains a
separate problem. No nonzero knot scalar or general filling
asymptotic follows from the sign theorem alone.

The two complete direct texts were read, their directly used
identities checked, and their pins verified:

* [Physical Jacobi charge boundary](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_physical_jacobi_charge_boundary.md),
  SHA256 530425b0c4504f2512954438465deb6d9a6e322fa58c641b6c678161baae6583:
  exact row recurrence, normalization and valid physical index range.
* [Exact signed-turn identities](research_full_endpoint_unit_turn_identities.md),
  SHA256 e2f69aaff28080b9dd9e11365ce18d68a9d738667917204714556681c50789e8:
  full canonical algebra, triangular signed turn and ordinary reproducer.

The positivity proof and finite coefficient recursion are derived
above. No named orthogonal-polynomial positivity theorem, numerical
evaluation, mathematical program, test or compilation is used.
Adopted notes and public manuscripts are unchanged.
