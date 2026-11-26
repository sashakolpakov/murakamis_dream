# Quantitative reconstruction from the actual cyclotomic source jets

Private written proof, 23 November 2026.

The exact bounded-jet Mellin theorem has a quantitative version for
every specified actual arithmetic operator in that theorem. Its loss
is at most \(e^{CN^2}\). When the leading coefficient is a product of
nonconstant clock binomials, the loss improves to \(N^Ae^{CN}\).
Both bounds include singular steps and preserve the original prefix,
affine source, pole lattice and residue.

The extra factor hypothesis is not proved for every Conway operator.
No geometric approximate section is constructed, and no volume identity
or arbitrary-short-filling theorem follows.

## 1. Actual source and the optional factor hypothesis

Use the complete \(Q\)-only conventions of [M]:
\[
 P=\sum_{j=0}^{d}a_j(Q,Y)T^j,\qquad TY=QYT,\qquad
 \sum_{j=0}^{d}a_j(Q,Q^m)C_{m+j}(Q)=0,\quad m\ge1.
 \tag{1}
\]
Here \(d\ge1\), the \(C_r\) are the actual reduced color periods,
and the fixed \(a_j\) are Laurent polynomials over a fixed number field
after one recorded denominator clearing. Retain their actual source
and normalization. Let \(A_Q,D,s\) be the \(Q\)-span, \(Y\)-span, and
number of collected monomials of \(a_d\). For the general bound take
\(B=D(s-1)\), \(k=B+1\), and \(n_0\ge d+A_Q+1\) as in [M].
Larger fixed jet orders are allowed.

For the sharper bound suppose additionally that
\[
 a_d(Q,Y)=cQ^uY^v
       \prod_{t=1}^{p}(1-Q^{a_t}Y^{b_t})^{m_t},
 \quad c\ne0,\quad b_t\ne0,\quad m_t\ge1,
 \tag{2}
\]
with all exponents integral and fixed. Empty products are allowed.
Put
\[
 M=\sum_t m_t,\qquad B_0=\sum_t m_t|b_t|.
 \tag{3}
\]
In this case it suffices to use any fixed \(k\ge B_0+1\).
Increase \(n_0\) so \(a_t+b_t(r-d)\ne0\) whenever \(r\ge n_0\).
There are only finitely many excluded integer trajectories.

The original formal section and source are
\[
 Z(Q,X)=\sum_{r\ge n_0}C_r(Q)X^r,\qquad P^MZ=\mathcal B,
\]
\[
 P^M=\sum_{j,\ell}a_{j,\ell}(Q)Q^{-\ell j}X^{-j}S^\ell,
 \qquad Sf(X)=f(QX).
 \tag{4}
\]
The source \(\mathcal B\) is fixed by the actual \(d\)-color prefix.
No quantum normal of that prefix is reset.

Write \(Q_N=e^{2\pi i/N}\), \(Z_N=Z(Q_N,\cdot)\), and
\[
 p_{<,N}(X)=\sum_{r=1}^{n_0-1}C_r(Q_N)X^r.
\]
The exact original cyclotomic lattice and closing in [M] are
\[
 (1-X^N)(Z_N+p_{<,N})\in X\mathbb C[X],\quad\deg\le N,
 \qquad K_N=\operatorname{Res}_{X=\infty}Z_N\,\frac{dX}{X}.
 \tag{5}
\]
This retains the polynomial part at infinity as well as finite poles.

## 2. Scaled jets and the quantitative statement

Use \(Q=Q_N(1+\zeta/N)\), and let \(R_h=\mathbb C[\zeta]/\zeta^h\).
For \(v=\sum_{j<h}v_j\zeta^j\), set \(\|v\|_h=\sum_{j<h}|v_j|\).
This norm is submultiplicative and decreases under truncation.
These are actual quantum jets, with a specified change of scale.

Let \(W_N\) be a rational section in \(X^{n_0}\mathbb C[[X]]\)
satisfying the same pole/prefix lattice
\[
 (1-X^N)(W_N+p_{<,N})\in X\mathbb C[X],\qquad\deg\le N.
 \tag{6}
\]
Suppose coefficients \(w_r(\zeta)\in R_k\), \(n_0\le r\le N\),
lift its root coefficients and retain the actual \(d\)-color prefix
through order \(k-1\). Set \(w_r=0\) for \(r<n_0\). Assume
\[
 \left\|[X^m]\left(P^M\sum_{r=n_0}^{N}w_rX^r-\mathcal B\right)
       \right\|_k\le\delta_N,\qquad n_0-d\le m\le N-d.
 \tag{7}
\]
All coefficients and \(\mathcal B\) in (7) are evaluated at the
displayed scaled \(Q\); its Fourier ordering remains (4).

Let \(\mathcal E_N\) be the maximum of the two quantities
\[
 \max_{n_0\le r\le N}|[X^r](W_N-Z_N)|,\qquad
 \left|\operatorname{Res}_{\infty}W_N\frac{dX}{X}-K_N\right|.
\]
**Theorem.** Constants depending only on the fixed operator,
prefix and jet order satisfy, for all sufficiently large \(N\),
\[
 \boxed{\quad \mathcal E_N\le C_1e^{C_2N^2}\delta_N.\quad} \tag{8a}
\]
Under (2) there is the sharper bound
\[
 \boxed{\quad \mathcal E_N\le C_1N^Ae^{C_2N}\delta_N,\quad
                         A=1+kMB_0.\quad}                \tag{8b}
\]
Exact defect zero recovers uniqueness. Sections 3--5 prove the
refinement; Section 6 gives the general arithmetic bound.

## 3. The full-orbit denominator estimate

Fix integers \(a,b\) with \(b\ne0\), and put \(g=\gcd(|b|,N)\).
As \(r\) runs through \(0,\ldots,N-1\), its phase coset occurs \(g\)
times. Factoring \(z^{N/g}-1\) proves
\[
 \prod_{\substack{0\le r<N\\Q_N^{a+br}\ne1}}
       |1-Q_N^{a+br}|=
 \begin{cases}
 (N/g)^g,&g\mid a,\\
 |1-e^{2\pi ia/g}|^g,&g\nmid a.
 \end{cases}                                                   \tag{9}
\]
In the first case use the derivative at the omitted root one.
Since \(g\) belongs to the finite divisor set of \(|b|\), (9)
is at least a constant \(c_{a,b}>0\), independent of \(N\).
Every factor is at most two. Hence every subset of the nonzero
orbit factors, including any consecutive propagation segment, obeys
\[
 \prod_{r\in I}|1-Q_N^{a+br}|\ge c_{a,b}2^{-N}.
 \tag{10}
\]
The same lower bound holds for products of their minima with one:
apply (10) to just the factors below one.

For \(h_r(\zeta)=a_d(Q,Q^{r-d})\), each vanishing binomial has
order one. Its integer exponent \(E=a_t+b_t(r-d)\) is nonzero
by the choice of \(n_0\). The total order lost through \(r=N\) is
\[
 \sum_{r=n_0}^{N}\mu_r\le B_0,\qquad
                 \mu_r=\operatorname{ord}_{\zeta=0}h_r.
 \tag{11}
\]
Indeed the congruence \(a_t+b_t(r-d)\equiv0\pmod N\) has at most
\(\gcd(|b_t|,N)\le|b_t|\) solutions in a window of length at most \(N\).

## 4. Regular and singular jet inverses

Every coefficient \(a_j(Q,Q^m)\), \(n_0-d\le m\le N-d\),
has uniformly bounded \(R_k\) norm. To see this termwise, its
substituted monomials have exponent \(E=O(N)\), and
\[
 [\zeta^\ell](1+\zeta/N)^E=\binom E\ell N^{-\ell}
 \tag{12}
\]
is uniformly bounded for every fixed \(\ell<k\), also for negative
integer \(E\). Fixed Laurent coefficients and their finite sums
therefore have one common bound.

If \(\mu_r=0\), the finite geometric inverse in \(R_k\) gives
\[
 \|h_r^{-1}\|_k\le C\max(1,|h_r(0)|^{-k}).
 \tag{13}
\]
Its proof writes \(h_r=h_r(0)+v\), \(v\in\zeta R_k\), and sums
\(h_r(0)^{-1}\sum_{\ell=0}^{k-1}(-v/h_r(0))^\ell\).
The uniform coefficient bound proves (13).
By (2), (10), and the unit moduli of the monomials, the product
of the right sides of (13) over all regular steps is at most \(e^{CN}\).
This uses the complete orbit product, not a worst pivot bound per step.

At a singular step factor \(h_r=\zeta^{\mu_r}u_r\).
A vanishing factor has first scaled coefficient \(-E/N\);
because \(E\) is a nonzero multiple of \(N\), its modulus is at
least one. Every nonvanishing root factor has modulus at least
\(2\sin(\pi/N)\ge4/N\). Thus
\[
 |u_r(0)|\ge c'N^{-M},\qquad
 \|u_r\|_{k-\mu_r}\le C,\qquad
 \|u_r^{-1}\|_{k-\mu_r}\le C N^{kM}.
 \tag{14}
\]
The quotient coefficients are bounded by (12), shifted by the
fixed vanishing order. Only \(B_0\) steps can be singular.

## 5. Propagation with exactly the available precision

Subtract the actual truncated jets and write their errors as \(e_r\).
The exact Fourier ordering in (4) cancels the shift offset, giving
\[
 \sum_{j=0}^{d}a_j(Q,Q^{r-d})e_{r-d+j}=\rho_{r-d},
                         \qquad \|\rho_{r-d}\|_k\le\delta_N.
 \tag{15}
\]
All initial prefix errors vanish. Put
\(M_r=\sum_{t=n_0}^{r}\mu_t\), \(h(r)=k-M_r\ge1\).
At step \(r\), retain earlier errors only through precision
\(k-M_{r-1}\). These coefficients are already known: earlier
steps retained at least that precision.

At a regular step use (13). At a singular step the right side,
after subtracting earlier terms, is divisible by \(\zeta^{\mu_r}\)
modulo the available precision, since it equals \(h_re_r\).
Drop those first \(\mu_r\) zero coefficients and use (14).
This determines and bounds \(e_r\) in \(R_{h(r)}\).
No unavailable higher error jet is used or divided at zero.

The coefficient bounds (12), fixed memory \(d\), and triangle
inequality now give a discrete forced estimate: its amplification
is bounded by the product of fixed regular-step constants, the
regular inverse factors (13), and the singular factors (14).
There are at most \(N\) forcing terms. By (10)--(14) this is
\[
 \max_{r\le N}\|e_r\|_{h(r)}
               \le C N^{1+kMB_0}e^{CN}\delta_N .
 \tag{16}
\]
For precision, take at each step the maximum of all earlier
retained error norms; it is bounded by \(L_r(E+\delta_N)\),
where \(L_r\ge1\) is a fixed constant times the applicable inverse
bound. Iterating gives \(N\delta_N\prod_r L_r\), proving (16).

Finally \(H=(1-X^N)(W_N-Z_N)\) has degree at most \(N\).
Its coefficients through degree \(N\) are exactly \(e_r(0)\),
since both sections start in degree \(n_0>0\).
At infinity its quotient has constant term \(-e_N(0)\).
Thus its residue against \(dX/X\) is \(e_N(0)\), proving (8b).

## 6. The general arithmetic bound

Drop (2), and use \(B=D(s-1)\), \(k\ge B+1\).
Multiply the whole equation and its source by one fixed nonzero integer
so all Laurent coefficients are algebraic integers in a fixed number
field \(K\). Constants absorb this recorded rescaling.
This is possible by clearing the finitely many algebraic denominators.

Put \(h=[K:\mathbb Q]\). At a regular step the pivot
\(\lambda=a_d(Q_N,Q_N^{r-d})\ne0\) is an algebraic integer in
\(K(Q_N)\), whose degree is at most \(h\varphi(N)\le hN\).
All of its conjugates have modulus at most one fixed \(H\ge1\):
an embedding sends roots of unity to roots of unity, and the finitely
many coefficient conjugates have a fixed sum-of-moduli bound.
The field norm of a nonzero algebraic integer is a nonzero integer.
Its modulus is at least one. Bounding all factors except the specified
embedding by \(H\) therefore proves
\[
                         |\lambda|\ge H^{-hN}.             \tag{17}
\]
The integer-norm assertion can also be seen from the monic integral
minimal polynomial: its nonzero constant term is the signed product
of its conjugates. Passing to the larger field only raises that
integer product to a positive integral power.

The zero-step budget is the exact one in [M]. Because \(r-d>A_Q\),
the trajectory polynomial \(a_d(Q,Q^{r-d})\) is nonzero identically.
Its order \(\mu_r\) at \(Q_N\) is at most \(s-1\), by the
logarithmic-derivative Vandermonde argument. For all large \(N\),
\(a_d(Q_N,Y)\) is not identically zero. Its \(Y\)-span is \(D\)
and the visited \(Q_N^{r-d}\) are distinct. Hence at most \(D\)
indices vanish, and \(\sum_r\mu_r\le B\).

At such an index write the first nonzero scaled coefficient as
\[
 \beta_{\mu_r}=N^{-\mu_r}
       \sum_{a,b}c_{a,b}Q_N^{a+b(r-d)}
                         \binom{a+b(r-d)}{\mu_r}.           \tag{18}
\]
The sum \(N^{\mu_r}\beta_{\mu_r}\) is a nonzero algebraic integer.
Each of its conjugates is bounded by \(CN^{\mu_r}\), since generalized
binomial coefficients of integral exponents are integers and the
exponents are \(O(N)\). The same norm argument yields
\[
 |\beta_{\mu_r}|\ge
 N^{-\mu_r}(CN^{\mu_r})^{-hN}
                       \ge \exp[-C'N\log(N+1)].             \tag{19}
\]
The uniformly bounded scaled coefficients (12) and the inverse proof
(13) now bound each regular inverse by \(e^{CN}\), and each
singular unit inverse by \(e^{CN\log(N+1)}\).
The precision argument (15) is unchanged, with \(B\) replacing \(B_0\).
There are at most \(N\) regular steps and at most \(D\) singular steps.
Their product and the \(N\) forcing terms are bounded by \(C_1e^{C_2N^2}\).
The exact residue argument after (16) proves (8a).

## 7. Necessity of the refinement hypothesis and scope

Factors independent of \(Y\) cannot be admitted silently.
For the actual unknot colors \(C_r=1\), the all-level annihilator
\[
 P=[((1-Q)T-1)(T-1)]=hT^2-(1+h)T+1,\qquad h=1-Q,
\]
has jet budget one in [M]. Put \(h_N=1-Q_N\).
Fix \(r_0\ge n_0+2\) and set
\(e_r=0\) below \(r_0\), \(e_r=h_N^{N-r}\) through \(N\).
Its only finite-window defects are \(\pm h_N^{N-r_0+1}\);
its last coefficient is one. Adding
\((\sum_{r=r_0}^Ne_rX^r)/(1-X^N)\) preserves the exact prefix
and pole lattice but changes the residue by one.
The defect is \(\exp(-N\log N+O(N))\). Thus (8b) is false for
general factorizations allowing \(b=0\).
This is a test of a nonminimal actual annihilator, not a knot counterexample.

The general bound uses no binomial or classical-end hypothesis.
It applies to the specified arithmetic actual recurrence and source
of [M]. The finite-array elimination [F] does not prove (2) for every
knot, and primitive/Weyl symmetry does not eliminate the classical
end losses in [E]. No broad Conway factorization is asserted.
A geometric comparison must still produce (6)--(7) with its actual
source and sufficiently small defect. No such comparison is supplied.

All three complete matching texts were read; only written proofs
and text/hash operations were used. Frozen and public files are unchanged.

| Role | Complete source | SHA-256 |
| --- | --- | --- |
| M, input, 212 lines | [Exact cyclotomic jet uniqueness](mellin_cyclotomic_jet_uniqueness.md) | bf9fc91f4a4795b67b164b2828ebe5109f59fcb97adc2664846a98ee690090f2 |
| E, coverage, 324 lines | [Actual operator end loss](research_actual_operator_end_loss_and_coefficient_space.md) | d4b516e508e461f8cf9d617476622bd4c1c2e59cf6d26e7655a845064ae0d4ea |
| F, coverage, 343 lines | [Actual finite-sum annihilator](finite_sum_annihilator.md) | d6e973b5f43049d7e68b35bd32b6677871815c240c97e74b2a6bed3e00370ae3 |
