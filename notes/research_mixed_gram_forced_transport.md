# Exact forced transport for the two-cap Gram polynomial

Research deduction, 5 November 2026. The finite Gram polynomial has an
explicit inhomogeneous transport equation. Its forcing exceeds the
regular factorial-ratio phase at an actual open two-four reference.
Consequently that polynomial cannot have a separate uniform local
packet with the regular phase there. This is not a failure of the exact
two-cap identity, of a complete open-word sum, or of its conjectured
asymptotic.

## 1. The original polynomial and its exact forcing

Use the [two-cap identity](research_mixed_two_cap_torus_composition.md),
with \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and
\[
 G_N(X,Y)=\sum_{\ell=0}^{N-1}
 \frac{r^\ell(X^{-1};r)_\ell(Y^{-1};r)_\ell}{P_\ell^2}.
                                                               \tag{1}
\]
Both Laurent bands are \([-N+1,0]\). Its physical values are
\[
 K_N(a,b)=G_N(r^a,r^b)
 =r^{-ab}\frac{P_{a+b}}{P_aP_b}\,\mathbf1_{a+b<N}.       \tag{2}
\]
The quotient in (2) is used only on its support.

**Theorem 1.** For every \(N\ge2\), as a Laurent identity,
\[
 (1-rX)G_N(rX,Y)-(Y^{-1}-rX)G_N(X,Y)
   =\frac{1-Y^{-N}}{N^2}(X^{-1};r)_{N-1}.               \tag{3}
\]
The symmetric equation is obtained by interchanging \(X,Y\).
Away from \(1-rX=0\), this is equivalently
\[
 G_N(rX,Y)=\frac{Y^{-1}-rX}{1-rX}G_N(X,Y)
 -\frac{rX(1-X^{-N})(1-Y^{-N})}{N^2(1-rX)^2}.           \tag{4}
\]
The quotients in (4) are merely a convenient local notation for the
polynomial identity (3). No term on its right is discarded.

*Proof.* On the physical grid, (2) implies
\[
 (1-r^{a+1})K_N(a+1\bmod N,b)
 =(r^{-b}-r^{a+1})K_N(a,b).                              \tag{5}
\]
For \(a<N-1\), this is the factorial recurrence on the triangle;
at its last surviving row the multiplier on the right vanishes.
For \(a=N-1\), the left multiplier is zero, and the right side
is zero both when \(b=0\) and when \(b>0\).

Let \(D(X,Y)\) be the left side of (3). Its potential \(X^1\)
coefficient cancels: the two shifted polynomials have the same
constant coefficient in \(X\). Hence its \(X\)-band is still
\([-N+1,0]\); its \(Y\)-band is \([-N,0]\). Equation (5)
and interpolation in \(X\) imply \(D(X,r^b)=0\) identically
in \(X\). Thus
\(D(X,Y)=(Y^{-N}-1)d(X)\).

Only the last term of (1) contributes to its \(Y^{-(N-1)}\)
coefficient. Since \(P_{N-1}=N\) and the leading coefficient
of \((A;r)_{N-1}\) is
\((-1)^{N-1}r^{(N-1)(N-2)/2}=r\), this coefficient is
\((X^{-1};r)_{N-1}/N^2\). The coefficient of \(Y^{-N}\)
in \(D\) is its negative. This proves (3). Finally
\[
 (X^{-1};r)_{N-1}
       =\frac{1-X^{-N}}{1-r^{-1}X^{-1}}
\]
gives (4). All statements retain both parities. \(\square\)

## 2. The regular homogeneous phase and the forcing rate

Put \(X=e^{-2\pi ia}\), \(Y=e^{-2\pi ib}\). The phase
obtained from the physical factorial quotient in (2) is
\[
 W(a,b)=J(a+b)-J(a)-J(b)+i\pi ab,                        \tag{6}
\]
where \(J(0)=0\) and \(J'=\operatorname{Log}(2\sin\pi z)\)
on the original sine strip. Indeed the physical factorial phase is
\(g(z)=J(z)+i\pi z(1-z)/2\), and
\(g(a+b)-g(a)-g(b)+2\pi iab=W(a,b)\).
Its derivative satisfies the unforced transport identity
\[
 e^{W_a(a,b)}=\frac{Y^{-1}-X}{1-X}.                     \tag{7}
\]
Neither (6) nor (7) identifies an off-grid finite sum with the
homogeneous factorial continuation.

On a compact set where \(\Im a,\Im b<0\) and \(X,Y\ne1\),
the magnitude of the forcing in (4) has the exact exponential rate
\[
 B(a,b)=-2\pi(\Im a+\Im b).                            \tag{8}
\]
This follows from
\((1-X^{-N})(1-Y^{-N})=X^{-N}Y^{-N}(1+o(1))\), uniformly
when the two negative heights are bounded away from zero; the
remaining factors have polynomial size. More generally its upper
rate is \(2\pi([ -\Im a]_++[-\Im b]_+)\), with actual zeros
on some real physical nodes. The strict negative-height case (8)
does not have that qualification.

**Corollary 2.** If \(B(a,b)>\Re W(a,b)\) at such a point,
there is no neighborhood on which, for fixed constants \(C,L\),
\[
 |G_N(e^{-2\pi ia'},e^{-2\pi ib'})|
       \le C N^L e^{N\Re W(a',b')}                     \tag{9}
\]
holds for all sufficiently large levels. In particular a nonzero
uniform regular-phase packet, with a fixed polynomial power, is
impossible there.

For a proof apply (9) at \((a,b)\) and \((a+1/N,b)\), which
both remain in the same neighborhood. Holomorphy of \(W\) gives
\(N[W(a+1/N,b)-W(a,b)]=O(1)\). All coefficients on the left
of (3) are uniformly bounded, so its rate is at most \(\Re W\).
Its right side has rate (8), a contradiction. No lower bound on
\(G_N\) is used.

## 3. A certified actual two-four reference

Take the open word \((4,4)\). Reversal symmetry and the proved
[global open-word uniqueness](research_mixed_open_word_hessian.md)
allow its two private legs to be equal to \(e\), its two attached
legs to be equal to \(t\), and its endpoint auxiliaries to be equal
to \(u\), once a root of the original equations is exhibited.
Those equations are
\[
\begin{split}
 0={}&-J'(e-u)+J'(e+t)-J'(e)+i\pi(u-t+e-1/2),\\
 0={}&J'(e+t)+J'(2t)-3J'(t)+i\pi(2t-e-1/2),\\
 0={}&2\operatorname{Log}\cos\pi u+
       \operatorname{Log}\sin\pi(e-u)
       -3\operatorname{Log}\sin\pi u+i\pi e.
\end{split}                                                   \tag{10}
\]
They are the original endpoint map with external input \(b=t\),
not an exponentiated or altered lift. Its Jacobian equals that of
the endpoint map with \(b\) fixed, with the additional entry
\(\pi\cot(2\pi t)+i\pi\) in the \((t,t)\) position.

The focused checker supplies one rational product disk of radius
\(10^{-10}\), centered at
\[
\begin{split}
 e_0&=.34631393520098791-.038944335631581867i,\\
 t_0&=.31130778505506168-.062275178143913874i,\\
 u_0&=.22618679546498327+.034903800154668048i.
\end{split}                                                   \tag{11}
\]
It verifies a genuine original-log Newton contraction with a fixed
rational inverse, on the enclosing derivative squares. The disk
stays in the proved \(E\times Q\times U\) chamber and the
attached disk \(D_4\). Hence it is the unique actual \((4,4)\)
reference, including against nonsymmetric roots.

On its whole enclosure, outward arithmetic proves
\[
 \Re W(t,t)<.461,\qquad -4\pi\Im t>.782,
 \qquad -4\pi\Im t-\Re W(t,t)>8/25.                    \tag{12}
\]
For orientation the last difference is approximately \(.3224706\).
Thus Corollary 2 applies at an actual attached pair, rather than
merely at a corner of an enclosing rectangle.

## 4. Scope and reproduction

The exact two-cap torus identity still holds. It includes all of (1),
and both original factors \(d_N(X)(1+X^{-N})\) where prescribed.
The result excludes the separate regular-phase estimate (9), not
cancellation of the forced sectors after a complete Fourier
projection. It also does not exclude a different asymptotic for
\(G_N\). The retained one-cap representation and a terminal
conditional packet are another possible source route.

The checker uses one fixed original-log disk and exact transport
algebra. It proposes no roots and performs no parameter cover:

```sh
python3 experiments/check_mixed_gram_forced_transport.py --precision 256
python3 experiments/check_mixed_gram_forced_transport.py --precision 320 --input repro/results/research-mixed-gram-forced-transport.json --output repro/results/research-mixed-gram-forced-transport-replay.json
```
