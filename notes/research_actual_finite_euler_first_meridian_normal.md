# The actual first meridian normal of the finite Euler polynomial

Private written proof, 18 November 2026.

The paired finite Euler polynomial has an inhomogeneous first-normal
equation. On a sufficiently small positive-action sector its actual
normal has the same exponential as the root polynomial, multiplied by
an explicit \(N\log N\) factor. The vacuum source fixes this factor;
it is not removed by solving a homogeneous equation. On the opposite
small half-plane the same actual normal tends to \(1/t\), whereas the
root polynomial is exponentially small.

The sole complete direct C, pinned below, proves the local unit
asymptotic for the actual finite root polynomial. The coefficient
normal, analytic multiplier estimate, finite-product remainder, and
source integral are proved here. No conclusion about the complete
opposite kernel or a geometric source contribution is made.

## 1. Actual finite family and the exact forcing

Put
\[
 c_0=2\pi i,\quad Q=e^{c_0/N},\quad d=N-1,\quad
 f_n=(Q;Q)_n,\qquad
 E_{v,N}(t)=\sum_{n=0}^{d}\frac{t^n}{(vQ;Q)_n}.
 \tag{1}
\]
This is the actual truncated polynomial, meromorphic in \(v\).
Its root value is \(E_N=E_{1,N}\). Every denominator is nonzero
near \(v=1\) for a fixed \(N\). The coordinate
\(v=Q^{-\nu}=e^{-c_0\nu/N}\) gives a common pole-free disk
\(|\nu|<1/4\). We assert an asymptotic only for its first normal.

Consecutive coefficients, including the top coefficient, give
\[
 (1-t)E_{v,N}(t)-vE_{v,N}(Qt)
       =1-v-\frac{t^N}{(vQ;Q)_d}.
 \tag{2}
\]
Set
\[
 S_{n,N}=\sum_{j=1}^n\frac{Q^j}{1-Q^j},\quad S_{0,N}=0,
 \qquad
 H_N(t)=\left.\partial_vE_{v,N}(t)\right|_{v=1}
       =\sum_{n=0}^d S_{n,N}\frac{t^n}{f_n}.
 \tag{3}
\]
Pairing \(j\) with \(N-j\) gives \(S_{d,N}=-d/2\);
when \(N\) is even the middle term is \(-1/2\).
Since \(f_d=N\), differentiating (2) yields exactly
\[
 (1-t)H_N(t)-H_N(Qt)
       =E_N(Qt)-1+\frac{d}{2N}t^N,\qquad H_N(0)=0.
 \tag{4}
\]
Both the vacuum and the upper forcing are retained.

Use logarithms continued from zero to define
\[
 \mathcal S(t)=-\operatorname{Li}_2(t)/c_0,\qquad
 y(t)=t\mathcal S'(t)=\operatorname{Log}(1-t)/c_0,\qquad
 g(z)=\frac{e^{c_0z}-1}{c_0z},\quad g(0)=1.
 \tag{5}
\]
C proves on a fixed small disk the actual finite identity
\[
 E_N(t)=e^{N\mathcal S(t)}A_N(t),\qquad
 A_N(t)=(1-t)^{-1/2}(1+O(N^{-1})).
 \tag{6}
\]
Here \(A_N,A_N^{-1}\) are uniformly bounded holomorphic functions
on a slightly smaller disk for large \(N\), with all fixed
derivatives bounded there. C's proof compares the literal Taylor
cap with \(e^{L_N}\) by an exponentially small relative error.

**Theorem.** There is \(r>0\) such that, uniformly on every compact
\(\mathcal K\Subset\{t:0<|t|<r,\ \operatorname{Im}t<0\}\),
\[
 \boxed{\quad
 -\frac{c_0}{N}\frac{H_N(t)}{E_N(t)}
   =\log N+\gamma+\operatorname{Log}(-t/c_0)+O(N^{-1}).
 \quad}\tag{7}
\]
The logarithm on the right is the one on the right half-plane;
\(-t/c_0\) has positive real part. The constant
\(\gamma=\lim_{n\to\infty}(\sum_{j=1}^n j^{-1}-\log n)\)
is Euler's constant. All fixed \(t\)-derivatives of the normalized
error obey the same order on smaller compact sets.

In particular \(H_N\) is nonzero on each such compact set for
large \(N\), and
\[
 H_N(t)=-\frac{N}{c_0}(1-t)^{-1/2}e^{N\mathcal S(t)}
 \bigl[\log N+\gamma+\operatorname{Log}(-t/c_0)+O(N^{-1})\bigr]
 (1+O(N^{-1})).
 \tag{8}
\]
The two errors in (8) have their displayed separate meanings;
(7) is the sharper ratio statement.

**Complementary theorem.** After reducing the same \(r\) if needed,
uniformly on every compact
\(\mathcal K_+\Subset\{t:0<|t|<r,\ \operatorname{Im}t>0\}\),
\[
 \boxed{\qquad
 |E_N(t)|\le C e^{-cN},\qquad
 H_N(t)=\frac1t+O(N^{-1}).
 \qquad}\tag{8a}
\]
The second error has the same order after every fixed number of
\(t\)-derivatives on smaller compact sets. In particular this actual
normal is nonzero there for large \(N\). It has a larger exponential
order than the root value. The proof below retains the divided
difference at \(x=1\) in (26), so it does not separate two divergent
endpoint integrals.

## 2. Coefficient tails

We will need tail estimates before using cancellation.
For \(1\le j<N\),
\[
 |1-Q^j|\ge 4\min(j,N-j)/N.
 \tag{9}
\]
These inequalities imply the convenient all-index bound
\[
                         |f_n|\ge N^{-n}n!,\qquad n<N.
 \tag{10}
\]
For \(n\le N/2\), multiply the lower-half factors in (9).
For \(n>N/2\), the product of the first \(n\) integers
\(\min(j,N-j)\), divided by \(n!\), is
\[
 \frac{\binom{d}{n}}{\binom{d}{\lfloor d/2\rfloor}}
 \ge 2^{-d}.
 \]
Indeed the omitted tail product is \((d-n)!\), and the full
product is \(\lfloor N/2\rfloor!\lfloor(N-1)/2\rfloor!\).
Now \(4^n\ge2^d\), proving (10). Also
\[
 |S_{n,N}|\le C N\log(N+1),\qquad
 \sum_{n=0}^d|t^n/f_n|\le e^{N|t|}.
 \tag{11}
\]
The first estimate follows by summing the reciprocals in (9).

Fix \(0<\rho<1\). For sufficiently small \(r\), uniformly
on \(|t|\le r\),
\[
 \sum_{\rho N<n<N}|t^n/f_n|\le e^{-bN}.
 \tag{12}
\]
The constant \(b\) can be made arbitrarily large by reducing \(r\).
For a direct proof, (10) bounds the tail by that of
\(\sum (Nr)^n/n!\); the first term is at most
\((er/\rho)^{\rho N+O(1)}\), and the successive ratios
are at most \(r/\rho+o(1)<1\).
Multiplication by any fixed power of \(N\), by \(\log(N+1)\),
or by \(C^{\delta N}\) does not obstruct this choice.

On the small disk of (6), \(|E_N(t)|^{-1}\le C e^{C N r}\).
Thus the coefficient tails in (12) may also be made
exponentially small relative to \(E_N\). This observation will
be used only after fixing the constants in the following lemma.

## 3. An analytic multiplier lemma

Fix a disk \(|z|<R\) on which \(g\) is a holomorphic unit.
Let \(F_N(z)\) be any family holomorphic on that disk with
\(\sup|F_N|\le B\), uniformly in \(N\).
There are fixed \(0<\rho<R/8\) and a sufficiently small \(r>0\),
independent of this family, such that
\[
 \boxed{\quad
 \sum_{n\le\rho N}F_N(n/N)\frac{t^n}{f_n}
       =E_N(t)\bigl[F_N(y(t))+O(B/N)\bigr],
                    \qquad |t|\le r.
 \quad}\tag{13}
\]
Floors are understood in finite sums. The constants may depend
on the fixed disks, but not on \(F_N\).

Here is a proof retaining the long Taylor remainder. For a fixed
\(t\), the centered moment generating function is exactly
\[
 e^{-y(t)z}\frac{E_N(te^{z/N})}{E_N(t)}.
 \tag{14}
\]
On \(|z|\le\epsilon N\), (6) and Taylor's formula for
\(\mathcal S(te^{z/N})\) give the bound
\[
 \left|e^{-yz}\frac{E_N(te^{z/N})}{E_N(t)}\right|
       \le C\exp(C|z|^2/N).
 \tag{15}
\]
The linear term cancels because \(y=t\mathcal S'(t)\).
All arguments stay in the unit disk of (6) after choosing
\(\epsilon\) and then \(r\) small.
Consequently the exact centered moments
\[
 M_k(t)=\frac1{E_N(t)}
         \sum_{n=0}^d(n/N-y(t))^k\frac{t^n}{f_n}
 \]
satisfy
\[
 M_0=1,\quad M_1=O(N^{-1}),\qquad
 |M_k|\le (Ck/N)^{k/2}\quad(2\le k\le\delta N).
 \tag{16}
\]
For the latter bound apply Cauchy's estimate to (14) on a
circle of radius a fixed constant times \(\sqrt{kN}\);
reduce \(\delta\) so this radius is at most \(\epsilon N\),
and use \(k!\le k^k\). The improved first moment follows
directly from
\(M_1=N^{-1}t\,\partial_t\log A_N(t)\).

Expand \(F_N\) about \(y(t)\) through degree \(K-1\),
\(K=\lfloor\delta N\rfloor\). Take \(|y(t)|<\rho\).
Cauchy's formula on a fixed disk about \(y\) supplies
coefficient bounds \(B R_0^{-k}\), for some fixed \(R_0>4\rho\).
For \(k\ge2\) the resulting moment sum is bounded by
\[
 B\sum_{k=2}^{K-1}R_0^{-k}(Ck/N)^{k/2}=O(B/N).
 \tag{17}
\]
To check the sum, the ratio of its consecutive majorants is
at most \(e^{1/2}\sqrt{C(k+1)/(NR_0^2)}\); reduce \(\delta\)
so it is at most \(1/2\). The \(k=1\) term is \(O(B/N)\)
by (16).

The actual expansion is used first on \(n\le\rho N\).
Its remainder there is at most \(CBq^K\), with
\(q=2\rho/R_0<1\). Dividing its weighted sum by \(E_N\)
costs at most \(C e^{C N r}\), by (11) and (6).
Choose \(r\) so that this remainder is exponentially small.
Replacing the truncated moments of the Taylor polynomial by
the full moments in (16) costs at most
\[
 B e^{-bN+C N r+C'\delta N},
 \]
by (12), since \(|n/N-y|^k\le C^k\) and \(k\le\delta N\).
Again reduce \(r\) after \(\rho,\delta\) are fixed.
The omitted constant-moment tail has the same bound.
These choices prove (13), including its long Taylor remainder.
Reduce \(r\) once for any remaining finitely many small levels:
\(E_N(0)=1\) makes them zero-free on a common smaller disk.
They are then harmless after increasing constants.

The lemma is a cancellation-preserving estimate. A uniform
\(O(N^{-1})\) error in individual coefficients, with no analytic
multiplier structure, would not suffice for (13).

## 4. The finite-product correction has that analytic structure

Let \(h_n=\sum_{j=1}^n j^{-1}\), \(h_0=0\), and set
\[
 b(z)=\frac{c_0 e^{c_0z}}{e^{c_0z}-1}-\frac1z
                       =\partial_z\log g(z).
 \tag{18}
\]
The singularity at zero is removable. For integer \(n<N\)
there is the exact identity
\[
 -\frac{c_0}{N}S_{n,N}-h_n
                     =\frac1N\sum_{j=1}^n b(j/N).
 \tag{19}
\]
We now construct an analytic interpolation of this last sum
to exponential accuracy on \(n\le\rho N\); it is only a
tool for estimating the original coefficients.

Choose nested disks \(|z|<R<R_1<1\) on which \(b\) is
holomorphic, with a fixed buffer between them. For an integer
\(L\ge1\), define
\[
 \begin{split}
 F_{N,L}(z)={}&\log g(z)+\frac{b(z)-b(0)}{2N}\\
 &+\sum_{\ell=1}^{L}
 \frac{B_{2\ell}}{(2\ell)!\,N^{2\ell}}
       \bigl[b^{(2\ell-1)}(z)-b^{(2\ell-1)}(0)\bigr].
 \end{split}\tag{20}
\]
The Bernoulli numbers here are defined by
\(w/(e^w-1)=\sum B_j w^j/j!\).
For \(L=\lfloor\alpha N\rfloor\), with \(\alpha>0\)
sufficiently small, there are constants \(a,C>0\) such that
\[
 \sup_{|z|\le R}|F_{N,L}(z)-\log g(z)|\le C/N,
 \tag{21}
\]
\[
 \left|\frac1N\sum_{j=1}^n b(j/N)-F_{N,L}(n/N)\right|
                      \le C e^{-aN},\qquad n\le\rho N.
 \tag{22}
\]

We give the remainder control explicitly. Repeated integration
by parts with the periodic Bernoulli polynomials on the cells
\([j/N,(j+1)/N]\) gives the endpoint formula (20), with
remainder bounded by
\[
 \frac{C\rho}{N^{2L}}
       \frac{\sup_{0\le x\le1}|B_{2L}(x)|}{(2L)!}
       \sup_{0\le z\le\rho}|b^{(2L)}(z)|.
 \tag{23}
\]
This follows first for one cell from \(B_j'=jB_{j-1}\);
the nonconstant endpoint terms telescope between cells,
and the first Bernoulli polynomial gives the half-endpoint
term in (20). Keeping the term with index \(L\) and this
remainder is the usual integration-by-parts formula.

For completeness the generating function
\(w e^{xw}/(e^w-1)\) is uniformly holomorphic on a fixed
circle \(|w|=b_0<2\pi\), \(0\le x\le1\).
Cauchy's estimate therefore gives
\[
 |B_j(x)|/j!\le C b_0^{-j}.
 \]
Cauchy on the fixed buffer for \(b\) gives
\(|b^{(j)}|\le C j! a_0^{-j}\).
Thus (23) is at most
\[
 C(2L)!\,(N b_0 a_0)^{-2L}
       \le C\left(\frac{2L}{N b_0a_0}\right)^{2L}.
 \tag{24}
\]
Choose \(\alpha\) to make the last base strictly less than one.
This proves (22). The same estimates on the slightly smaller
complex disk bound each term of (20) by
\(C(2\ell-1)!(N b_0a_0)^{-2\ell}\).
Their consecutive majorants have ratio at most a fixed
number less than one for \(\ell\le L\), after reducing
\(\alpha\). Their sum is \(O(N^{-2})\); the explicit
half-endpoint term is \(O(N^{-1})\). This proves (21)
as a holomorphic bound, not merely on the sampled real indices.

Apply (13) to the uniformly bounded analytic family \(F_{N,L}\).
Equations (19)--(22), the tails (11)--(12), and a final reduction
of \(r\) give
\[
 \frac1{E_N(t)}
 \sum_{n=0}^d
 \left(-\frac{c_0}{N}S_{n,N}-h_n\right)\frac{t^n}{f_n}
                       =\log g(y(t))+O(N^{-1}).
 \tag{25}
\]
Indeed the exponentially small sampled error in (22) costs
at most \(e^{C N r}\), and the discarded high indices cost
only the \(O(\log N)\) bound from (11) and \(h_n\).
All parameter choices can therefore be made successively:
the analytic disks, \(\rho,\delta,\alpha\), and finally \(r\).

## 5. The harmonic integral retains the vacuum

For the literal polynomial there is the exact finite identity
\[
 \sum_{n=0}^d h_n\frac{t^n}{f_n}
       =\int_0^1\frac{E_N(t)-E_N(xt)}{1-x}\,dx.
 \tag{26}
\]
It follows by integrating
\((1-x^n)/(1-x)=1+\cdots+x^{n-1}\).
The apparent endpoint singularity cancels. In particular
the term \(E_N(0)=1\) has not been reset.

Let \(\mathcal K\) be as in the theorem, and write
\(u=1-x\). On a slightly enlarged such compact set,
\[
 \operatorname{Re}[t\mathcal S'(xt)]
       =\frac{\arg(1-xt)}{2\pi x}>0,\qquad 0\le x\le1,
 \tag{27}
\]
with its continuous positive limit at \(x=0\).
It has a uniform positive lower bound. Hence, with
\(\Delta_t(u)=\mathcal S(t)-\mathcal S((1-u)t)\),
\[
 \operatorname{Re}\Delta_t(u)\ge c u,\qquad
 \Delta_t(u)=y(t)u+O(u^2),\qquad \operatorname{Re}y(t)\ge c.
 \tag{28}
\]
The amplitude ratio from (6) is
\[
 R_{N,t}(u)=A_N((1-u)t)/A_N(t)=1+O(u),
 \tag{29}
\]
uniformly, by its holomorphic unit bounds.
Consequently (26), divided by \(E_N(t)\), differs from
\[
 I(Ny)=\int_0^1\frac{1-e^{-Ny u}}u\,du
 \tag{30}
\]
by \(O(N^{-1})\). On a fixed small \(u\)-interval, the
difference of exponentials is bounded by
\(CNu^2e^{-c'Nu}\), using (28), and (29) contributes
\(Cu e^{-c'Nu}\). After division by \(u\), their integral
is \(O(N^{-1})\). On the rest of the interval both
exponentials have a uniform exponential bound.

On a right half-plane ray,
\[
 I(Ny)=\log N+\operatorname{Log}y+\gamma+O(e^{-cN}).
 \tag{31}
\]
One can fix its constant without an imported asymptotic:
compare \(I(n)\) with
\(h_n=\int_0^1(1-(1-u)^n)\,du/u\).
Their difference tends to zero, by the same endpoint comparison.
Thus \(I(n)-\log n\to\gamma\). Also
\(\partial_z[I(z)-\log z]=-e^{-z}/z\).
Integration towards infinity, then analytic continuation in
\(\operatorname{Re}z>0\), proves (31), uniformly for the
compact set of \(y\)'s in (28).
It follows that the actual harmonic multiplier equals
\[
 \frac1{E_N(t)}\sum_{n=0}^d h_n\frac{t^n}{f_n}
      =\log N+\operatorname{Log}y(t)+\gamma+O(N^{-1}).
 \tag{32}
\]
The portion of (26) near \(x=0\) involving \(E_N(xt)/E_N(t)\)
is exponentially subordinate by (28). Its exact presence,
together with \(H_N(0)=0\), nevertheless fixes the solution
and its constant. This is why (32) is not a consequence of
the homogeneous part of (4).

Combining (25) and (32), and using
\[
 y(t)g(y(t))=\frac{e^{c_0y(t)}-1}{c_0}=-t/c_0,
 \qquad
 \operatorname{Log}y(t)+\log g(y(t))
                  =\operatorname{Log}(-t/c_0),
 \tag{33}
\]
proves (7). The logarithmic equality follows near
\(t=-c_0a\), \(a>0\), and then throughout the small lower
half-disk by continuation. Holomorphy and Cauchy's estimates
on enlarged compact subsets give the derivative assertion.

### The opposite half-plane and the vacuum layer

On an enlarged compact set \(\mathcal K_+\) from (8a), the sign in
(27) is reversed:
\[
 \operatorname{Re}[t\mathcal S'(xt)]\le-c<0,\qquad 0\le x\le1.
 \tag{33a}
\]
The limit at zero is still taken continuously. Hence
\(\operatorname{Re}\mathcal S(xt)\le-cx\). In particular (6)
gives the exponential estimate for \(E_N(t)\) in (8a).
The analytic multiplier result (25) remains valid here: its proof
was on the whole small disk and did not use a half-plane sign.

Write
\(\mathfrak h_N(t)=\sum_{n=0}^d h_n t^n/f_n\), and split its exact
integral (26) at \(x=1/2\). For \(1/2\le x\le1\), use
\[
 \frac{E_N(t)-E_N(xt)}{1-x}
       =\frac{t}{1-x}\int_x^1 E_N'(st)\,ds.
 \tag{33b}
\]
By (6),(33a), \(|E_N'(st)|\le C N e^{-cN/2}\) on that
interval, after harmlessly decreasing \(c\). Thus the whole
second integral is \(O(N e^{-cN/2})\). Its numerator stays
together; neither separated \(1/(1-x)\) integral is used.

For \(0\le x\le1/2\), the contribution of \(E_N(t)\) is
exponentially small. Set \(a=t/c_0\), whose real part is
uniformly positive on \(\mathcal K_+\). The exact amplitude
in (6) satisfies \(A_N(0)=1\) and uniformly bounded first
derivatives, so
\[
 \frac{A_N(xt)}{1-x}=1+O(x),\qquad
 \mathcal S(xt)=-a x+O(x^2).
 \tag{33c}
\]
Both \(\mathcal S(xt)\) and \(-a x\) have real part at most
\(-c'x\). The integral formula for the difference of their
exponentials therefore bounds that difference by
\(C N x^2e^{-c'Nx}\). Consequently
\[
 \begin{split}
 \int_0^{1/2}\frac{E_N(xt)}{1-x}\,dx
 &=\int_0^{1/2}e^{-Nax}\,dx
       +O\!\left(\int_0^{1/2}(x+Nx^2)e^{-c'Nx}\,dx\right)\\
 &=\frac{c_0}{Nt}+O(N^{-2}).
 \end{split}\tag{33d}
\]
It follows, with the original vacuum value still one, that
\[
 \mathfrak h_N(t)=-\frac{c_0}{Nt}+O(N^{-2}).
 \tag{33e}
\]
Finally (25) says
\[
 -\frac{c_0}{N}H_N(t)
   =\mathfrak h_N(t)
      +E_N(t)\bigl[\log g(y(t))+O(N^{-1})\bigr].
 \tag{33f}
\]
The second term is exponentially small on \(\mathcal K_+\).
Equations (33e)--(33f) prove \(H_N(t)=1/t+O(N^{-1})\).
All estimates hold on enlarged compact subsets, so holomorphy
and Cauchy's estimates prove the fixed-derivative assertion.
This is an actual vacuum-generated normal sector, rather than
a solution selected from the homogeneous part of (4).

## 6. Actual normal coordinates and source scope

Write \(\mathcal E_{\nu,N}(t)=E_{Q^{-\nu},N}(t)\).
The exact adapters are
\[
 \left.\partial_\nu\mathcal E_{\nu,N}\right|_0
      =-\frac{c_0}{N}H_N,\qquad
 v=M^{-2}.
 \tag{34}
\]
For the scaled meridian \(M=e^{u/N}\), \(\nu=2u/c_0\);
for the unscaled meridian \(\mu=\log M\), \(\nu=2N\mu/c_0\).
Therefore (7) gives, with
\(B_N(t)=\log N+\gamma+\operatorname{Log}(-t/c_0)\),
\[
 \left.\frac{\partial_\nu\mathcal E_{\nu,N}}{E_N}\right|_0
          =B_N(t)+O(N^{-1}),
 \tag{35}
\]
\[
 \left.\frac{\partial_u E_{e^{-2u/N},N}}{E_N}\right|_0
          =\frac2{c_0}\bigl[B_N(t)+O(N^{-1})\bigr],
 \qquad
 \left.\frac{\partial_\mu E_{e^{-2\mu},N}}{E_N}\right|_0
          =\frac{2N}{c_0}\bigl[B_N(t)+O(N^{-1})\bigr].
 \tag{36}
\]
At \(M=1\), \(\partial_M=\partial_\mu\).
These are derivatives of the literal finite denominator family
in (1) at fixed \(q_N\); no root reflection was differentiated.
The \(t^N\) forcing in (4) remains exact and is controlled
by the actual coefficient and Taylor-cap estimates.

On the upper-half-plane compact sets of (8a), the same exact
adapters instead give the absolute normal estimates
\[
 \left.\partial_\nu\mathcal E_{\nu,N}\right|_0
    =-\frac{c_0}{Nt}+O(N^{-2}),\qquad
 \left.\partial_u E_{e^{-2u/N},N}\right|_0
    =-\frac2{Nt}+O(N^{-2}),\qquad
 \left.\partial_\mu E_{e^{-2\mu},N}\right|_0
    =-\frac2t+O(N^{-1}).
 \tag{36a}
\]
These are not ratios to the exponentially small root value.
Thus the positive-action condition is essential to (32);
(8a) explicitly exhibits the larger normal sector on the other
side. No estimate across a Stokes boundary is asserted.
The theorem does not assert a
uniform approximation on a fixed \(\nu\)-disk, a higher
meridian-normal expansion, or any quantum-parameter normal.

Finally (1) is one paired donor factor. Its external scalar
lines, coupon, turnover, quotient, and original closing
functional remain separate actual factors. The derivatives
above hold \(t\) fixed: an actual argument \(t(M)\), an
external factor such as \(E_A(M)\), and \(q_F(M)\) retain
their own terms in the full product and chain rules. Equations
(7),(8a),(35)--(36a) do not identify a geometric frame in either
sector, estimate their convolution, or prove noncancellation
of the complete source.

## Complete proof direct

* C: notes/research_factorial_coupon_small_activity_saddle.md,
  SHA256 9ab9fef5bfab21872aa9c6ec72990e9695df24e5cfffddb02902aaced4e16465.

The complete direct was freshly read nontruncated in this
active author sequence. Every used implication was checked.
Only written mathematics and text/hash operations were used.
Frozen and public files were not edited.
