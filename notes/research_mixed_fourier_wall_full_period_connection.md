# Exact full-period continuation and a reflected Wall solution

Research deduction, 7 November 2026. Cancellation in the finite
coefficients before specializing the base gives an exact terminal
value for the Wall degree recurrence. It also identifies the associated
finite Jacobi matrix with a weighted cyclic shift. A reflected Wall
polynomial supplies an explicit independent solution and a nonzero
connection determinant at the original Fourier parameter.

These are finite algebraic statements. The reflected solution uses
the inverse base and a shifted argument; the completed half-degree
asymptotic does not already estimate it. No numerical value, root,
source bound or recurrence is evaluated here.

## 1. Cancel first, then specialize

Let \(N\ge2\), \(r=e^{-2\pi i/N}\), and \(|a|<1\). Keep the
argument \(u\) distinct from the parameter \(a\). For a generic
nonzero base \(q\), the finite coefficient identity is
\[
 \frac{(q^{-n};q)_l}{(q;q)_l}
   =(-1)^lq^{-nl+l(l-1)/2}{n\brack l}_q ,
 \qquad 0\le l\le n.
 \tag{1}
\]
The Gaussian binomial on the right is a polynomial in \(q\);
its polynomial definition follows, for example, by induction from
the finite product
\[
 \prod_{j=0}^{n-1}(1+q^jz)
   =\sum_{l=0}^n q^{l(l-1)/2}{n\brack l}_q z^l.
 \tag{2}
\]
Define the canceled specialization, for every integer \(n\ge0\), by
\[
 {\cal W}_n(u;a)=
 \sum_{l=0}^n
 \frac{(-1)^l r^{-nl+l(l-1)/2}{n\brack l}_r}
      {(ar;r)_l}\,u^l.
 \tag{3}
\]
All denominators in (3) are nonzero. For \(n<N\), this is exactly
the original \(W_{n,N}(u;a)\), with no change of normalization.
For \(n\ge N\), (3) specifies a continuation; it does not interpret
an uncanceled \(0/0\) coefficient.

At \(n=N\), (2) and
\(\prod_{j=0}^{N-1}(1+r^jz)=1-(-z)^N\) show that the intermediate
Gaussian binomials vanish. The top coefficient in (3) has sign
\[
 (-1)^N r^{-N(N+1)/2}
       =(-1)^N(-1)^{N+1}=-1.
 \tag{4}
\]
Since \((ar;r)_N=1-a^N\), it follows that
\[
 \boxed{\displaystyle
 {\cal W}_N(u;a)=1-\frac{u^N}{1-a^N}.}
 \tag{5}
\]
This computation includes both level parities.

Use the exact coefficients of the
[original degree recurrence](research_mixed_fourier_right_cap_wall_endpoint_strip.md):
\[
 A_n=r^n(1-ar^{n+1}),\qquad
 C_n=ar^n(1-r^n),\qquad
 B_n=A_n+C_n-u/r.
 \tag{6}
\]
The generic finite coefficient proof there applies to every \(n\):
it is an identity of rational functions of a generic base before
specialization. After (1) cancels the Gaussian factors, both sides
are regular at \(q=r\). Consequently
\[
 A_n{\cal W}_{n+1}=B_n{\cal W}_n-C_n{\cal W}_{n-1}
 \quad(n\ge0),\qquad {\cal W}_0=1,
 \tag{7}
\]
with the absent \(n=0\) term understood through \(C_0=0\).
This proves the recurrence at \(n=N-1,N\) as well; those cases
are not obtained by dividing by a vanished coefficient.

The coefficients are \(N\)-periodic, \(A_n\ne0\), and \(C_N=0\).
At \(n=N\), (7) gives
\[
 {\cal W}_{N+1}={\cal W}_N
        \left(1-\frac{u}{r(1-ar)}\right)
        ={\cal W}_N{\cal W}_1 .
 \tag{8}
\]
Induction in the periodic recurrence therefore proves
\[
 \boxed{\displaystyle
 {\cal W}_{N+k}={\cal W}_N{\cal W}_k\quad(k\ge0),\qquad
 {\cal W}_{mN+k}={\cal W}_N^{\,m}{\cal W}_k
 \quad(m\ge0,\ 0\le k<N).}
 \tag{9}
\]
No division by \({\cal W}_N\) is needed for (9).

At the original diagonal \(u=a=Y\), the inherited \(|Y|<5/8\)
and \(N\ge2\) give
\[
 {\cal W}_N(Y;Y)=\frac{1-2Y^N}{1-Y^N}\ne0,
 \tag{10}
\]
because \(2|Y|^N\le2(5/8)^2<1\). This terminal nonvanishing
does not assert that every intermediate value is nonzero.

## 2. An exact cyclic matrix model

Let \(J=J_N(a)\) act on vectors indexed by \(0,\ldots,N-1\):
\[
 (Jv)_n=r\{A_n(v_n-v_{n+1})+
                      C_n(v_n-v_{n-1})\}.
 \tag{11}
\]
Here \(v_N=0\), and the \(n=0\) second term is absent.
Let \(T\) be the lower triangular coefficient matrix
\[
 T_{nl}=[u^l]\,W_{n,N}(u;a),\qquad 0\le n,l<N .
 \tag{12}
\]
Its diagonal entries are nonzero by (1), so \(T\) is invertible.
Define the weighted cyclic shift
\[
 (Cv)_n=v_{n+1}\quad(n<N-1),\qquad
 (Cv)_{N-1}=(1-a^N)v_0.
 \tag{13}
\]

**Proposition 1.** One has
\[
 JT=TC,\qquad J^N=(1-a^N)I,\qquad
             \det(uI-J)=u^N-(1-a^N).
 \tag{14}
\]

*Proof.* Put \(v(u)=(1,u,\ldots,u^{N-1})^T\) and
\(W(u)=Tv(u)\). Recurrence (7) gives
\[
 (J-uI)W(u)=(1-a){\cal W}_N(u;a)e_{N-1}.
 \tag{15}
\]
The last diagonal coefficient of \(T\) is
\[
 T_{N-1,N-1}=\frac1{(ar;r)_{N-1}}
                          =\frac{1-a}{1-a^N},
 \tag{16}
\]
where the numerator sign is again canceled exactly. Thus
\[
 (C-uI)v(u)=(1-a^N-u^N)e_{N-1}
\]
and (5), (15)--(16) prove \(JT=TC\) as a polynomial identity
in \(u\). Equation (13) gives the remaining statements directly.
\(\square\)

The eigenvalues are the \(N\) distinct roots of \(1-a^N\);
the corresponding eigenvectors are \(W(u)\). This is an explicit
finite cyclic representation, not an assertion that \(T\) and its
inverse have subexponential norms. In particular it does not turn
an operator norm or averaged lower bound into a lower bound for a
specified component \(W_n(Y;Y)\).

For completeness, away from \(u^N=1-a^N\), the exact resolvent is
\[
 (J-uI)^{-1}
 =\frac{\displaystyle\sum_{d=0}^{N-1}u^dJ^{N-1-d}}
              {1-a^N-u^N}.
 \tag{17}
\]
Combining with (15) cancels the scalar denominator and recovers
the polynomial vector
\[
 W(u)=\frac{1-a}{1-a^N}
              \sum_{d=0}^{N-1}u^dJ^{N-1-d}e_{N-1}.
 \tag{18}
\]
The identity extends to all \(u\) by polynomial equality.

## 3. A reflected solution and its connection determinant

Assume now \(a\ne0\). Let \(W_k^{(-)}\) denote the original
finite Wall polynomial with base \(r^{-1}\), for \(0\le k<N\).
Set
\[
 \begin{split}
 G_k&=a^{-k}\frac{(a/r;r^{-1})_k}{(r^{-1};r^{-1})_k},\\
 {\cal B}_{N-1-k}
   &=G_k W_k^{(-)}(u/r;a)\quad(0\le k<N),\\
 {\cal B}_N&=0.
 \end{split}
 \tag{19}
\]
Every \(G_k\) is finite and nonzero. In particular
\({\cal B}_{N-1}=1\). The inverse base and argument \(u/r\)
in (19) are both essential.

**Proposition 2.** The sequence \({\cal B}\) satisfies the same
recurrence (7) for \(1\le n\le N-1\). For \(0\le n<N\),
\[
 \begin{split}
 {\cal D}_n
 &:=W_n{\cal B}_{n+1}-W_{n+1}{\cal B}_n\\
 &=-{\cal W}_N
                 \prod_{j=n+1}^{N-1}\frac{A_j}{C_j}.
 \end{split}
 \tag{20}
\]
In particular
\[
 {\cal D}_0=
 -\frac{1-a^N-u^N}{N a^{N-1}(1-ar)} .
 \tag{21}
\]
At \(u=a=Y\), every determinant in (20) is nonzero.

*Proof.* Write \(z=r^{-k}\), \(n=N-1-k\), and
\({\cal B}_{n}=G_kv_k\). The ratio
\[
             \frac{G_{k+1}}{G_k}
                =\frac{1-az/r}{a(1-z/r)}
 \tag{22}
\]
converts the reversed recurrence into \(r^{-1}\) times the Wall
degree recurrence with base \(r^{-1}\), parameter \(a\), and
argument \(u/r\). Its two off-diagonal coefficients become
\[
 r^{-1}z(1-az/r),\qquad r^{-1}az(1-z),
\]
and its diagonal coefficient becomes
\[
 r^{-1}\{z(1+a)-a(1+r^{-1})z^2-u\}.
 \tag{23}
\]
These are exactly the required three coefficients. At \(k=0\),
the backward neighbor is \({\cal B}_N=0\), and the initial
Wall equation gives that same endpoint recurrence directly.
No \(G_N\), whose displayed denominator would vanish, is used.

The Casoratian of any two solutions satisfies
\({\cal D}_n=(C_n/A_n){\cal D}_{n-1}\) for \(1\le n<N\).
Here \({\cal D}_{N-1}=-{\cal W}_N\), proving (20).
Finally
\[
 \prod_{j=1}^{N-1}\frac{A_j}{C_j}
       =\frac{1-a^N}{N a^{N-1}(1-ar)}
 \tag{24}
\]
by the original cyclotomic products. Equations (5), (20) and
(24) give (21), and (10) proves the final assertion.
\(\square\)

Thus the actual forward solution and (19) form an exact basis
for the recurrence on \(0,\ldots,N\), when only the interior
equations \(1\le n<N\) are imposed. The first endpoint equation
selects the actual forward solution; the terminal Dirichlet
condition selects (19). Their determinant is known explicitly
and nonzero at the original parameter.

The terminal value alone does not initialize the backward
recurrence. Its other datum is explicitly
\[
 W_{N-1,N}(u;a)=\sum_{l=0}^{N-1}\frac{u^l}{(ar;r)_l},
 \tag{25}
\]
since \(r^{-(N-1)}=r\). If \({\cal R}_N=1\),
\({\cal R}_{N-1}=0\), and \({\cal R}\) is generated backwards
by the nonzero \(C_n\), then the exact reconstruction is
\[
 W_n={\cal W}_N{\cal R}_n+W_{N-1,N}{\cal B}_n .
 \tag{26}
\]
The first coefficient is proved nonzero at the original diagonal.
No nonvanishing or asymptotic estimate for the second coefficient
in (25) is inferred from (10).

## 4. Original source and the remaining connection problem

For the actual outgoing contraction, (3) is used only at
\(n=N-j-1<N\). Consequently the exact identity remains
\[
 H_{j,N}(y)=
 \frac{e^{-\pi i(N-1)y}(1-Y^N)}{N(1-Y)}
       P_j W_{N-j-1,N}(Y;Y).
 \tag{27}
\]
This is the [original Wall source](research_mixed_fourier_right_cap_wall_operator.md):
the lifted Fourier factor, \(1/N\), \(P_j\), and the index shift
are all unchanged. The canceled degree-\(N\) value is an algebraic
boundary condition for this recurrence, not an additional physical
row of the source.

The [completed half-degree theorem](research_mixed_fourier_right_cap_wall_half_degree_completion.md)
controls the actual forward solution on \(0\le n\le N/2\).
Formula (19) is an exact reflected solution on the other half,
but not a second application of that theorem: its base is inverted
and its argument is \(Y/r\) while its parameter remains \(Y\).
In the limiting recurrence, reversing the degree and multiplying
by the scalar \(G_k\) changes the two local characteristic roots
by inversion and a common nonzero factor. Equality of their
moduli is therefore preserved.

The [degree-monodromy theorem](research_mixed_fourier_wall_degree_monodromy.md)
proves such an equality somewhere in the original second half.
It consequently obstructs a uniformly contracting single-root
proof for the reflected half as well. The exact determinant
(20) supplies transversality of the finite forward and backward
solutions; it does not supply uniform asymptotics of the reflected
solution through this equal-modulus locus, nor nonzero individual
asymptotic connection coefficients.

What is now explicit is the canceled full-period continuation,
its cyclic matrix model, and a two-sided finite connection with
known nonzero determinant. Estimates through the remaining
two-branch region, or bounds for the actual component (25),
remain necessary before this route yields a new bound for the
coherently grouped low-retained-index source.
