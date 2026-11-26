# The complete first period over the early negative second interval

Private implication assembly, 11 November 2026. Both first Fourier
coefficients of the literal \(44\) polynomial are bounded after
attachment to the full second weight and the next own-four kernel
when the second coordinate lies on its early interval at its actual
negative height. The proof joins the already controlled first paths.
It adds no new analytic estimate and does not complete a second period.

All six direct inputs below are adopted at their stated scopes.
This is a separate implication assembly requiring its own independent review.

## 1. Exact polynomial and unchanged action

Fix the same actual positive three/four word of length \(m\ge4\)
beginning with \(444\) as the first-left and first-right sources.
Retain its coupled reference \(r_j=a_j+ic_j\), logarithmic lifts,
ordinary color, attached following leg and all normalizations.
Put
\[
 P=[11/50,9/20],\quad E=[1/10,11/50],\quad H=1/100,\qquad
 y=q+ic_2,\ q\in E,\quad z=u+ic_3,\ u\in P.                         \tag{1}
\]
The actual bounds \(c_2,c_3\in[-.102,-.001]\) and
\(-.078<c_1<-.020\) are inherited from these source families.
At \(m=4\), the third index is ordinary with its original attached
following leg; it is not replaced by a cap.

Write \(q_N=e^{-2\pi i/N}\), \(P_j=(q_N;q_N)_j\),
\(p_j(X)=(q_NX;q_N)_j\), and keep
\[
\begin{split}
 U_{1,N}(w,X)&=\sum_{i=0}^{N-1}H_N(w,q_N^{-i})p_i(X)/P_i^2,\\
 C_{1,N}(X,Y)&=\sum_{j=0}^{N-1}X^{-j}p_j(X)p_j(Y)/P_j^3,\\
 L_N(w;X,Y)&=U_{1,N}(w,X)d_N(X)C_{1,N}(X,Y),\\
 f^{(0)}_{44,N}(w,Y)&=N[X^0]L_N,\qquad
 f^{(1)}_{44,N}(w,Y)=N[X^N]L_N,\qquad
 f_{44,N}=f^{(0)}_{44,N}+f^{(1)}_{44,N}.                            \tag{2}
\end{split}
\]
The endpoint coefficient \(H_N\) and polynomial \(d_N\) are complete.
The latter has degree less than \(N\) and \(d_N(q_N^j)=P_j^{-1}\)
for every \(0\le j<N\).

The \(X\)-band of \(L_N\) is contained in \([-N+1,2N-2]\), so its
only multiples of \(N\) are zero and \(N\). The exact root filter gives
\[
 f_{44,N}(w,Y)=\sum_{j=0}^{N-1}
             \frac{U_{1,N}(w,q_N^j)}{P_j}C_{1,N}(q_N^j,Y).          \tag{3}
\]
This is the single unnormalized physical sum in the pointwise prefix
theorem, equation (3). There is no additional factor two, \(1/N\),
crossing scalar, or outgoing diagonal factor. Both degrees in \(w,Y\)
are at most \(N-1\).

For precision, use the original phases
\[
\begin{split}
 \Psi(e,a)&=S(e)+g(e+a)-g(a)-g(e)-\frac{i\pi}{2}(e-e^2),\\
 Q(s;a,b)&=g(s+a)+g(s+b)-3g(s)-g(a)-g(b)+2\pi ias,\\
 F_{123}&=\Psi(e,z_1)+Q(s_2;z_1,z_2)+Q(s_3;z_2,z_3)
                         -g(z_1)-g(z_2)-\tfrac12g(z_3),\\
 \Lambda_{123}(z)&=\Re F_{123,*}
       +\Re\{\partial_{z_3}F_{123,*}(z-r_3)\}.                    \tag{4}
\end{split}
\]
The star denotes the unchanged actual critical reference.
This equals the action written as \(L_1+\phi_2+\phi_3\) and its
outgoing marginal in all four path inputs. No primitive constant,
marginal, or cap normalization is changed.

Set \(Y=e^{-2\pi iy}\), \(Z=e^{-2\pi iz}\), and
\[
 K_{\sigma,N}(w;a,y)=L_N(w;e^{-2\pi ia},Y)e^{2\pi iN\sigma a},
 \qquad
 {\cal K}_{\sigma,N}=K_{\sigma,N}\,d_N(Y)C_{1,N}(Y,Z).
                                                                    \tag{5}
\]
Thus \({\cal K}_{\sigma,N}\) is exactly each input's complete
three-factor density. The second coordinate is unselected; no
\(Y^{-N}\) occurs in (5). Carry \(|d_N(Z)|^{1/2}\) as an exterior
modulus multiplier, including at its zeros.

## 2. Both complete first coefficient paths

For \(\sigma=0,1\), the exact coefficient integral is
\[
 f^{(\sigma)}_{44,N}(w,Y)
                  =N\int_0^1K_{\sigma,N}(w;a,y)\,da.               \tag{6}
\]
Every integrand is a finite Laurent polynomial in a nonvanishing
exponential, hence entire in the additive variable \(a\).
Define \(H_0=c_1,H_1=H\) and the successive oriented paths
\[
 {\cal H}_\sigma:\quad
 0\longrightarrow1/10\longrightarrow1/10+iH_\sigma
 \longrightarrow9/20+iH_\sigma
 \longrightarrow1/2+iH_\sigma
 \longrightarrow1/2\longrightarrow7/10\longrightarrow1 .          \tag{7}
\]
The point \(11/50+ic_1\) partitions the unselected horizontal into
its early and old-plateau pieces. The split at \(7/10\) is retained
only to match the original remainder decomposition.
Cauchy's theorem replaces \([0,1]\) in (6) by (7) exactly, for
each \(N,w,y\). Negative powers create no finite \(a\)-singularity.
The paths are fixed independently of \(N,w,y,z\).

Multiply this identity by \(d_N(Y)C_{1,N}(Y,Z)\), then retain the
outgoing modulus. Each path piece is paid by the following complete
finite-source inputs:

| First-path piece | Sector | Available gap below \(\Lambda_{123}\) |
|---|---|---:|
| \(0\to1/10\to1/10+iH_\sigma\to9/20+iH_\sigma\) | both | \(10^{-13}\), [complete first-left connection](research_mixed_complete44_second_early_first_left_connection.md), Theorem 1 |
| \(9/20+ic_1\to1/2+ic_1\to1/2\) | \(0\) | \(10^{-12}\), [unselected right connection](research_mixed_complete44_first_unselected_early_second_right_connection.md), Theorem (8) |
| \(9/20+iH\to1/2+iH\to1/2\) | \(1\) | \(\delta_R-\tau\), [selected right connection](research_mixed_complete44_first_selected_early_second_right_connection.md), Theorem (5) |
| \([1/2,1]\) | both | \(\delta_R/2-\tau\), [complete early-second real first arc](research_mixed_complete44_second_early_real_first_arc.md), Theorem (35) |

Here
\[
 \delta_R=\frac1{2500000}(9/20-a_1)^2>\frac1{250000000}.             \tag{8}
\]
The notation in the last two rows means the stated gap minus the
chosen source tolerance. Choose that tolerance below \(\delta_R/4\).
The same \(\Lambda_{123}\), full first weight, full second weight,
and outgoing halfweight occur in every entry. Each source has
already retained its complete cap and conditional rows, aliases,
joins, parity stops, endpoint forcing and genuine end groups.
In particular the last entry includes the closed endpoint one.

Take a finite intersection of the fixed ordinary-color disks and
their smaller derivative disks. Fixed path lengths and the original
single density \(N\,da\) cost only polynomial factors.
Thus, with for example
\[
                              \gamma_E=10^{-14},                 \tag{9}
\]
both coefficients satisfy
\[
 |f^{(\sigma)}_{44,N}(w,Y)d_N(Y)C_{1,N}(Y,Z)|\,|d_N(Z)|^{1/2}
 \le C N^B e^{N\{\Lambda_{123}(z)-\gamma_E\}}.                      \tag{10}
\]
Adding them costs a constant factor, so the same bound holds for
the whole \(f_{44,N}\):
\[
 \boxed{\;
 |f_{44,N}(w,Y)d_N(Y)C_{1,N}(Y,Z)|\,|d_N(Z)|^{1/2}
 \le C N^B e^{N\{\Lambda_{123}(z)-\gamma_E\}} .
 \;}                                                               \tag{11}
\]
Both level parities and all sufficiently large \(N\) are included,
uniformly for (1). Every fixed ordinary-color derivative has the
same rate on a smaller disk, with a polynomial prefactor.
The outgoing modulus multiplier is not differentiated or divided out.

## 3. The literal old plateau and its now-controlled remainder

For every complex \(y\), define exactly
\[
 I_{44,P,N}(w,y)=N\int_{P+ic_1}
 U_{1,N}(w,e^{-2\pi ia})d_N(e^{-2\pi ia})
                 C_{1,N}(e^{-2\pi ia},e^{-2\pi iy})\,da,
 \qquad
 R_{44,N}(w,y)=f_{44,N}(w,e^{-2\pi iy})-I_{44,P,N}(w,y).             \tag{12}
\]
This is the same \(I\) and \(R\) as in the pointwise prefix theorem.
Its plateau endpoints and height are fixed independently of \(w,y\).

Subtract the unselected old-plateau segment from the two exact
paths (7). The remainder is precisely the fourteen original
oriented currents: six left currents, three right currents for
each sector, and the two real currents from \(7/10\) to one.
Each still has its original \(+N\,da\) density and inherited
orientation. The common real segments remain two distinct
Fourier summands. Thus the same table proves directly
\[
 |R_{44,N}(w,y)d_N(Y)C_{1,N}(Y,Z)|\,|d_N(Z)|^{1/2}
 \le C N^B e^{N\{\Lambda_{123}(z)-\gamma_E\}}.                      \tag{13}
\]
There is no inference from a small signed first integral to
separate large integrands.

The prior early-central theorem already supplies, on this same
parameter set,
\[
 |I_{44,P,N}(w,y)d_N(Y)C_{1,N}(Y,Z)|\,|d_N(Z)|^{1/2}
 \le C N^B e^{N\{\Lambda_{123}(z)-10^{-11}\}}.                      \tag{14}
\]
Equations (12)--(14) display the exact residual identity and its
newly completed weighted bound. They do not assert an unweighted
bound for \(R_{44,N}\), obtained by dividing out a later factor.

## 4. Only the early unselected second interval

Define the literal next restricted integral
\[
 {\cal E}_{444,N}(w,Z)
 =N\int_{E+ic_2} f_{44,N}(w,e^{-2\pi iy})
             d_N(e^{-2\pi iy})C_{1,N}(e^{-2\pi iy},Z)\,dy .         \tag{15}
\]
It has increasing-real-part orientation and the original density
\(N\,dy\). Uniformity of (11) gives
\[
 |{\cal E}_{444,N}(w,Z)|\,|d_N(Z)|^{1/2}
 \le C N^B e^{N\{\Lambda_{123}(z)-\gamma_E\}},\qquad z\in P+ic_3.   \tag{16}
\]
Its color derivatives have the same scope. Expanding \(f_{44,N}\)
by (6)--(7) yields exactly the two original densities
\(N^2\,da\,dy\). The first full weight is consumed once in the
coefficient identity (2)--(3); the second full weight occurs once
in (15); the third outgoing halfweight is carried once.
Its other incidence belongs to the next original factor, including
the terminal transform at \(m=4\). All exterior unit scalars and
normalizations are unchanged.

The first period in (11)--(16) is complete. The second coordinate
is only on \(E+ic_2\), in its unselected sector. No continuation to
a smaller second real coordinate, a new second height, a selected
second complement, or a whole second period follows here.
No nonzero asymptotic for a complete next transfer, whole word,
knot, or arbitrary short filling is asserted.

## Direct source versions

| Direct source | SHA-256 |
|---|---|
| research_mixed_complete44_second_early_first_left_connection.md | f8b568de256d3ab6e6f8f47449506aae5b6e47dbe0e9ac3176465f4de5610c25 |
| research_mixed_complete44_first_unselected_early_second_right_connection.md | 3aea54d57e26013054ed51820bd0189dc549b13e7522ce8ed7efb082816b72b9 |
| research_mixed_complete44_first_selected_early_second_right_connection.md | 4a0ec064b1f408351088e386e3cba2c4bdf2ee852f2c3027687394fa0626ea58 |
| research_mixed_complete44_second_early_real_first_arc.md | ef9c322a418436d52015c90aea221a9ef602fda54cbe7aa1f96d3321c25cce11 |
| research_mixed_four_four_pointwise_prefix_replacement.md | 2a4a86ced4bb326baa2ca24bfd6f9c6846103070f4a0731f663ef6d2303a89b7 |
| research_mixed_complete44_second_early_central_four.md | e5be8082613eac6887d3aca857703e4ac5b511c430f35ca91fa388c71a924f45 |

The complete author proof and all six directly used source implications
have been read, and all six source hashes match. No mathematical
correction was needed. The note is author-frozen after final readback;
independent review of this separate assembly remains pending.
No mathematical numerical evaluation,
saved-value arithmetic, import, test, compilation or frozen-source
edit was used.

