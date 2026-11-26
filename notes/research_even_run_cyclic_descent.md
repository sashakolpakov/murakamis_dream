# Cyclic descent of the original even-run source

Research note, 3 November 2026.

The selected quantum eigenline of an even crossing run admits an
explicit horizontal section on the whole auxiliary disk. Its
normalization reproduces every original coefficient. The section
is algebraic; the only new scalar extension is an \(N\)-th root
of a nonvanishing classical function. At the physical orbit that
root contributes the bounded factor \(k^{j/N}\).

This is a finite cyclic descent construction with the original cap
retained. It determines a function whose values give the source,
but it does not yet estimate those values at the exponential scale.

## 1. The nonvanishing classical factor

Use the eigenvalues \(\mu_j(X)\) of
\(J_k(X)=T_k+E_{kk}+XE_{11}\) from the
[simple-spectrum theorem](research_even_run_simple_spectrum_and_marked_kernel.md).
Their labels satisfy \(\mu_j(1)=2\cos(j\pi/k)\), and they
are holomorphic and distinct on a disk \(|X|<R_k\), with
\(R_k>1\). Set
\[
 \nu_j(X)=1+X^2-X\mu_j(X),\qquad
 h_j(X)=X^{-1}\nu_j(X).
 \tag{1}
\]
The functions \(h_j\) are the eigenvalues of the classical
backward matrix. The elementary continuant determinant gives
\[
               \prod_{j=0}^{k-1}\nu_j(X)=1-X.
 \tag{2}
\]

**Lemma 1.** The function
\[
                    \psi_k(X)=\frac{\nu_0(X)}{1-X}
 \tag{3}
\]
extends holomorphically and without zeros to \(|X|<R_k\).
It has
\[
                  \psi_k(0)=1,\qquad \psi_k(1)=1/k.
 \tag{4}
\]
Its holomorphic logarithm \(\ell_k\), normalized by
\(\ell_k(0)=0\), is real on \([0,1]\), and
\(\ell_k(1)=-\log k\).

*Proof.* Every \(\nu_j(0)=1\). By (2) a zero can occur only
at \(X=1\). There
\(\nu_j(1)=4\sin^2(\pi j/(2k))\); only the factor with
\(j=0\) vanishes. The other factors have product \(k\),
so that zero is simple and \(\nu_0'(1)=-1/k\).
This proves (3)--(4) and the absence of any further zero.
A nonvanishing holomorphic function on a disk has a logarithm
with the stated normalization. Schwarz reflection follows from
the real coefficients and the eigenvalue labels at one. Thus
\(\psi_k\) is real and nonzero on \([0,1]\); it is positive
there since \(\psi_k(0)=1\). This fixes the value of its
logarithm at one. \(\square\)

At level \(N\), define the central function
\[
        a_{k,N}(X)=\exp\{-\ell_k(X)/N\}.
 \tag{5}
\]
It is the specified algebraic root
\(a_{k,N}^N=\psi_k^{-1}\), with \(a_{k,N}(0)=1\), and
\[
                  a_{k,N}(1)=k^{1/N}.
 \tag{6}
\]
For fixed \(k\), on every smaller closed disk,
\(a_{k,N}=1+O_k(N^{-1})\). Its logarithm and normalization
are part of the construction, not a choice made after evaluation.

## 2. Removing the universal factorial from the original transfer

Fix \(p=\sigma2k\), with \(k\ge1\) and
\(\sigma\in\{1,-1\}\). Put
\[
 q_\sigma=e^{\sigma\pi i/N},\quad Q_\sigma=q_\sigma^2,
 \quad \epsilon=(-1)^N,\quad X=x^N,
 \quad c_{k,N}(X)=q_\sigma a_{k,N}(X).
 \tag{7}
\]
Let \(H_0(x)=C_k(q_\sigma x)-q_\sigma^{-1}E_{kk}\).
The polynomial matrix from the
[original run transfer](research_two_run_source_transfer.md) gives
\[
 \mathcal P_N(x)
      =x^{-1}\mathcal B_k(q_\sigma x;q_\sigma)
      =x^{-1}(1-x)H_0(x)^{-1}.
 \tag{8}
\]
The inverse expression is used only on its regular set; the
explicit entries of \(\mathcal B_k\) show that (8) extends
polynomially. In particular
\[
 \deg\mathcal P_N\le2k-2,\qquad
 \mathcal P_N(0)=q_\sigma I,\qquad
 \det\mathcal P_N(x)=q_\sigma^k(1-x)^{k-1}.
 \tag{9}
\]

Let \(\Pi_N(x)\) be the selected projector from the marked-kernel
theorem, using \(q_\sigma\) for the negative sign, and let
\(E_x=\operatorname{im}\Pi_N(x)\). Its transport law is
\[
          \mathcal P_N(x)E_x\subseteq E_{Q_\sigma x}.
 \tag{10}
\]
The inclusion is equality at generic \(x\), and also at every
point of the physical orbit, as shown below.

**Lemma 2.** The ordered forward period of (8), restricted to
\(E_x\), is the scalar
\[
 \left.\mathcal P_N(Q_\sigma^{N-1}x)\cdots
          \mathcal P_N(x)\right|_{E_x}
           =-\psi_k(x^N)^{-1}I_{E_x}
           =c_{k,N}(x^N)^N I_{E_x}.
 \tag{11}
\]

*Proof.* On the regular set the full product of the original
backward matrices is \(B_N(x)\), in the order fixed in the
marked-kernel theorem. Multiplying the scalars in (8) gives
\[
 \mathcal P_N(Q_\sigma^{N-1}x)\cdots\mathcal P_N(x)
       =(-1)^{N-1}X^{-1}(1-X)B_N(x)^{-1}.
 \tag{12}
\]
The eigenvalue of \(B_N\) on \(E_x\) is
\(\epsilon h_0(X)=\epsilon X^{-1}(1-X)\psi_k(X)\).
Cancellation proves (11), including its minus sign. Both sides
are holomorphic on \(|x|<R_k^{1/N}\) after restriction by
\(\Pi_N\), so the identity extends through zero and the
physical orbit. Finally \(q_\sigma^N=-1\) and (5) give the
last equality. \(\square\)

## 3. An explicitly normalized horizontal section

A section means a vector-valued function with \(f(x)\in E_x\).
Call it horizontal when
\[
       f(Q_\sigma x)
          =c_{k,N}(x^N)^{-1}\mathcal P_N(x)f(x).
 \tag{13}
\]
Define the semilinear operator on such sections by
\[
 (\mathscr L f)(x)=c_{k,N}(x^N)^{-1}
           \mathcal P_N(Q_\sigma^{-1}x)f(Q_\sigma^{-1}x).
 \tag{14}
\]
Equation (11) says precisely that \(\mathscr L^N=I\).

Let \(u_0=(q_\sigma^{k-a})_{a=1}^k\) be the original
cap vector. Use the cardinal polynomial
\[
 d_Q(x)=\frac1N\sum_{r=0}^{N-1}(x/Q_\sigma)^r,
       \qquad g_N(x)=d_Q(x)\Pi_N(x)u_0.
 \tag{15}
\]
Thus \(d_Q\) is one at \(Q_\sigma\) and zero at every
other \(N\)-th root of unity. Form the unnormalized sum
\[
                 f_{p,N}(x)=\sum_{r=0}^{N-1}\mathscr L^r g_N(x).
 \tag{16}
\]
There is no further factor \(1/N\) in (16).

**Theorem 3.** The section (16) is algebraic and holomorphic
on \(|x|<R_k^{1/N}\), is horizontal, and satisfies
\[
                         f_{p,N}(Q_\sigma)=u_0.
 \tag{17}
\]
For all original colors \(0\le j<N\), set
\[
             F_{\sigma,j}=\prod_{r=1}^j(1-Q_\sigma^r),
                   \qquad F_{\sigma,0}=1.
 \tag{18}
\]
The original source vectors and coefficients are exactly
\[
 \boxed{\begin{aligned}
 u_j&=(-q_\sigma)^j k^{j/N}F_{\sigma,j}
                        f_{p,N}(Q_\sigma^{j+1}),\\
 (M^pe_0)_j&=\kappa^p(-q_\sigma)^j k^{j/N}F_{\sigma,j}
                        e_k^Tf_{p,N}(Q_\sigma^{j+1}),
 \qquad \kappa=\exp\frac{\pi i(N-1)^2}{2N}.
 \end{aligned}}                                               \tag{19}
\]
Every displayed section value is nonzero as a vector. The scalar
\(k^{j/N}\) lies between one and \(k\), independently of \(N\).

*Proof.* The matrices and projectors in (14)--(16) are holomorphic
on the indicated disk, and \(c_{k,N}\) has no zero there.
They are algebraic functions: the \(\mu_j\)'s satisfy the
classical characteristic polynomial, \(a_{k,N}\) satisfies
the specified root equation, and the construction uses finitely
many sums and products. Equation \(\mathscr L^N=I\) makes
(16) invariant under \(\mathscr L\), which is (13).

At \(x=Q_\sigma\), only the term with \(r=0\) survives
in (16), by the cardinal property in (15). The original cap
belongs to \(E_{Q_\sigma}\), so this term is \(u_0\).
Every matrix factor at the remaining physical points is finite.
Thus the normalization (17) includes its full scalar.

For \(j\ge1\), the actual forward equation reads
\[
      u_j=(1-Q_\sigma^{-j})
             \mathcal B_k(q_\sigma Q_\sigma^j;q_\sigma)u_{j-1}
          =(Q_\sigma^j-1)\mathcal P_N(Q_\sigma^j)u_{j-1}.
 \tag{20}
\]
Apply (13) successively, use \(c_{k,N}(1)=q_\sigma k^{1/N}\),
and start from (17). This proves the first line of (19);
the original coefficient identity gives the second. All factors
in (18) are nonzero in the stated range. The original \(u_j\)'s
are nonzero since the physical transfers before the reset are
invertible. This proves the final assertions. \(\square\)

At the reset, the same conclusion can be checked directly:
\[
 \mathcal P_N(1)=q_\sigma u_0u_0^T,
       \qquad u_0^Tu_D=\epsilon kN/q_\sigma.
 \tag{21}
\]
These identities give the required nonzero transport from the
last section value back to \(u_0\). In particular (13) has not
silently replaced the singular reset by an arbitrary invertible
matrix on the entire channel space.

Two nonzero meromorphic horizontal sections differ by a scalar
\(b(x^N)\). Indeed they generate the same one-dimensional line
at generic points; comparing (13) makes their quotient invariant
under \(x\mapsto Q_\sigma x\), so it descends to \(X=x^N\).
Cap normalization imposes \(b(1)=1\), which leaves an invariant
gauge away from the physical orbit. Formula (16) fixes a particular
section. No uniqueness among all cap-normalized meromorphic
sections is asserted.

## 4. The exact norm and the remaining exponential estimate

For a reflected even pair, let
\[
 S_j=\prod_{r=1}^j2\sin(\pi r/N),\qquad S_0=1.
\]
The original positive scalar is exactly
\[
 \boxed{\quad
 \phi_N(R^{-2k}T(R^{2k}))
    =\sum_{j=0}^{N-1} k^{2j/N}S_j^2
                 \bigl|e_k^Tf_{2k,N}(Q^{j+1})\bigr|^2.
 \quad}                                                       \tag{22}
\]
This follows from (19), the actual relation
\(\overline M=M^{-1}\), and the original Frobenius pairing.
It is an identity for the specified source, rather than a new
positive model. A gauge \(b(x^N)\) with \(b(1)=1\) leaves
every term unchanged.

The universal factorial contributes its known logarithmic
profile, and \(k^{2j/N}\) is bounded. The remaining rate in
(22) is therefore the rate of a specified algebraic section
sampled at the physical clock. That rate has not been determined
by the descent theorem.

There is a useful warning against reading a bulk growth rate
from one classical branch. Schwarz reflection gives
\(\nu_j(\overline X)=\overline{\nu_j(X)}\). The mean of
\(\log|\nu_j(e^{i\theta})|\) on the circle is zero: for
\(j>0\) this is the mean-value property of the nonvanishing
holomorphic function with \(\nu_j(0)=1\); for \(j=0\),
factor it as \((1-X)\psi_k(X)\) and use the same property
together with the integrable sine logarithm. Consequently, if
\[
 \begin{split}
 J(t)&=\int_0^t\log(2\sin\pi s)\,ds,\\
 B_j(t)&=\int_0^t\log|h_j(e^{2\pi is})|\,ds-2J(t),
 \end{split}
 \tag{23}
\]
then exactly
\[
                   B_j(1-t)=-B_j(t).
 \tag{24}
\]
The endpoint singularity of the selected branch is integrable.
These are identities for individual classical branch profiles,
not asymptotics for the original coefficients. A pointwise
spectral-radius bound can switch branches, and its full-circle
mean need not vanish.

The [odd-run descent theorem](research_odd_run_simple_spectrum_and_marked_kernel.md)
gives a complementary statement: odd runs have a unique primitive
polynomial horizontal section and no factorial in their sample
formula. Both parities now have explicit functions giving every
original coefficient with its normalization. A joined source
still pairs those coefficients coherently. The descent identities
do not turn that signed pairing into the positive sum (22), and
do not yet prove a volume identity for an untreated joined word.

## 5. A nowhere-zero algebraic horizontal frame

The particular section (16) may vanish away from the physical
orbit. Its zeros can be removed without changing a single original
coefficient.

**Corollary 4.** There is an algebraic horizontal section
\(\widehat f_{p,N}\), holomorphic and nowhere zero on
\(|x|<R_k^{1/N}\), with
\[
 \widehat f_{p,N}(Q_\sigma)=u_0,\qquad
 \widehat f_{p,N}(Q_\sigma^{j+1})
       =f_{p,N}(Q_\sigma^{j+1})\quad(0\le j<N).
 \tag{25}
\]
Consequently (19) and (22) hold unchanged with
\(\widehat f_{p,N}\) in place of \(f_{p,N}\).
No uniqueness of this frame is asserted.

*Proof.* First, every restricted one-step map
\(\mathcal P_N(x):E_x\longrightarrow E_{Q_\sigma x}\)
is nonzero on this disk. Otherwise its full ordered period
would annihilate \(E_x\), contrary to the nonzero scalar
in (11). Since these spaces are lines, the restricted map
is an isomorphism, including at the singular full-matrix
reset.

A nonzero component of the algebraic section \(f_{p,N}\)
has only finitely many zeros. Indeed take its irreducible
polynomial relation over \(\mathbb C(x)\), and clear
denominators. Its constant coefficient as a polynomial in
the component is a nonzero polynomial in \(x\); otherwise
irreducibility would force the component to be identically
zero. Every zero of that component is a zero of the constant
coefficient. Therefore the common zeros of all components
on the disk form a finite set.

Their multiplicities, defined as the minimum of the component
vanishing orders, are constant along each nonzero
\(Q_\sigma\)-orbit. This follows from (13), since its scalar
factor is nonzero and its restricted line map is an isomorphism
in local holomorphic frames. At zero, write
\(f_{p,N}(x)=x^r v+O(x^{r+1})\) with \(v\ne0\). The identities
\(\mathcal P_N(0)=c_{k,N}(0)I=q_\sigma I\) imply
\(Q_\sigma^r=1\), so \(N\) divides \(r\).

It follows that the monic polynomial recording exactly those
common zeros, with their multiplicities, is \(h(x^N)\)
for a polynomial \(h\). There is no common zero on the
physical orbit by Theorem 3, so \(h(1)\ne0\). Define
\[
          \widehat f_{p,N}(x)
              =\frac{h(1)}{h(x^N)}\,f_{p,N}(x).
 \tag{26}
\]
The apparent poles at the common zeros are removable by their
definition, and division removes every common zero in the disk.
The section remains algebraic. The scalar factor is invariant
under \(x\mapsto Q_\sigma x\), so horizontality is preserved.
It is one on the physical orbit, proving (25).
\(\square\)

Multiplication by a nonvanishing algebraic central function \(b(x^N)\)
with \(b(1)=1\) still changes such a frame away from the physical
orbit. Holomorphic nonvanishing does not give a uniform bound
as \(N\) varies, and this corollary does not estimate the rate
in (22).

The finite cyclic descent mechanism is classical Hilbert 90;
see Andrew V. Sutherland,
[Number Theory I, Lecture 24, Theorem 24.2 and Corollary 24.3](https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_full_lec.pdf#page=254).
No novelty is claimed for that mechanism. The source-specific
content here is the selected original period, its nonvanishing
central factor, the exact factorial and cap normalization, and
the resulting section's literal samples.

## 6. Reproducing the finite identity checks

The [checker](../experiments/check_even_run_cyclic_descent.py)
constructs the polynomial transfers and the literal cyclic average,
then compares the resulting samples with powers of the original
crossing matrix. It checks both signs, both level parities, and
channel dimensions larger than the level. It includes the singular
reset and two nonphysical central parameters.

```sh
python3 experiments/check_even_run_cyclic_descent.py --precision 150 --output repro/results/research-even-run-cyclic-descent-root.json
```

The [saved record](../repro/results/research-even-run-cyclic-descent-root.json)
contains 96 signed cases and 288 complete clock orbits. The largest
relative identity residual is less than \(3.80\cdot10^{-147}\).
These computations check the formulas and their normalization;
the all-level conclusions follow from the proofs above.
